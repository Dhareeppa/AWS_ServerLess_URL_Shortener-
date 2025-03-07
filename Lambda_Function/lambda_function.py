import json
import random
import string
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.table("UrlShortener")


def short_url_generate(length=6):
    char = string.ascii_letters + string.digits
    short_url = "".join(random.choices(char, k=length))
    return short_url


def stored_url(long_url):
    while True:
        short_code = short_url_generate()
        response = table.get_item(key={"short_code": short_code})
        if "Item" not in response:
            break

    table.put_item(Item={"short_code": short_code, "long_url": long_url})
    return short_code


def get_url(short_code):
    response = table.get_item(key={"short_code": short_code})
    return response["Item"]["short_code"]if "item" in response else None


def lambda_handler(event, context):
    http_method = event["httpMethod"]

    if http_method == "POST":
        body = json.loads(event["body"])
        long_url = body.get("long_url")
        if not long_url:
            return {"statuscode": 400, "body": json.dumps({"error": "Missing long_url"})}

        short_code = stored_url(long_url)
        return {"statuscode": 201, "body": json.dumps({"short_url": short_code})}

    elif http_method == "GET":
        short_code = event["pathParameters"]["short_code"]
        long_url = get_url(short_code)
        if long_url:
            return{
                "statuscode": 301,
                "headers" : {"Location": long_url},
                "body": json.dumps({"massage": "Redirecting...."})
            }
        else:
            return{"Statuscode": 404, "body": json.dumps({"error": "short url not found..."})}
    else:
        return {"statuscode": 405, "body": json.dumps({"error": "Method is Not Allowed..."})}




















