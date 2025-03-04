import json
import boto3
import random
import string
import urllib.parse

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("UrlMappings")


def is_valid_url(url):
    parse = urllib.parse.urlparse(url)
    return bool(parse.scheme and parse.netloc)


def generate_short_code(length=6):
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))


def lambda_handler(event, context):
    http_method = event["httpMethod"]
    if http_method == "POST":
        try:
            body = json.loads(event["body"])
            original_url = body.get("url")
            if not original_url or not is_valid_url(original_url):
                return {"statusCode": 400, "body": json.dumps({"error": "Valid_URL_Required"})}
            if not original_url:
                return {"statusCode": 400, "body": json.dumps({"error": "URL required"})}
            short_code = generate_short_code()
            table.put_item(Item={"short_code": short_code, "original_url": original_url})
            short_url = f"https://{event['requestContext']['domainName']}/{short_code}"
            return {"statusCode": 200, "body": json.dumps({"short_url": short_url})}
        except json.JSONDecodeError:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Invalid JSON body"})
            }
        except Exception as e:
            return {
                "statusCode": 500,
                "body": json.dumps({"error": f"Server Error {str(e)}"})
            }

    elif http_method == "GET":
        try:
            short_code = event["pathParameters"]["short_code"]
            response = table.get_item(Key={"short_code": short_code})
            item = response.get("Item")
            if not item:
                return {"statusCode": 404, "body": json.dumps({"error": "Not found"})}

            return {
                'statusCode': 301,
                'headers': {'Location': item['original_url']},
                'body': ''
            }
        except Exception as e:
            return {
                "statusCode": 500,
                "body": json.dumps({"error": f"Server error: {str(e)}"})
            }
    return {'statusCode': 400, 'body': json.dumps({'error': 'Invalid method'})}
