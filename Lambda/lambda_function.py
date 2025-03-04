import json
import boto3
import random
import string
import urllib.parse

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("UrlMappings")

def is_valid_url(url):
    parsed_url = urllib.parse.urlparse(url)
    return bool(parsed_url.scheme and parsed_url.netloc)

def generate_short_code(length=6):
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))

def lambda_handler(event, context):
    http_method = event.get("httpMethod")  # Avoid KeyError
    if not http_method:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Missing HTTP method"}),
            "headers": {"Content-Type": "application/json"}
        }

    if http_method == "POST":
        try:
            body = json.loads(event["body"])
            original_url = body.get("url")
            if not original_url or not is_valid_url(original_url):
                return {
                    "statusCode": 400,
                    "body": json.dumps({"error": "Valid URL required"}),
                    "headers": {"Content-Type": "application/json"}
                }
            short_code = generate_short_code()
            table.put_item(Item={"short_code": short_code, "original_url": original_url})
            short_url = f"https://{event['requestContext']['domainName']}/{short_code}"
            return {
                "statusCode": 201,
                "body": json.dumps({"short_url": short_url}),
                "headers": {"Content-Type": "application/json", "Location": short_url}
            }
        except json.JSONDecodeError:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Invalid JSON body"}),
                "headers": {"Content-Type": "application/json"}
            }
        except Exception as e:
            return {
                "statusCode": 500,
                "body": json.dumps({"error": f"Server error: {str(e)}"}),
                "headers": {"Content-Type": "application/json"}
            }

    # ... (GET handler and rest of the code remains unchanged)