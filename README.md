# 🚀 AWS Serverless URL Shortener

![AWS Serverless](https://img.shields.io/badge/AWS-Serverless-orange) ![Python](https://img.shields.io/badge/Python-3.x-blue) ![License](https://img.shields.io/badge/License-MIT-green)

A fully serverless URL shortener built with **AWS Lambda, DynamoDB, API Gateway, and S3**. This project allows users to shorten long URLs and provides redirection functionality without managing servers.

---

## 📌 Features
✅ Shorten long URLs instantly  
✅ Redirect users using short URLs  
✅ Serverless & auto-scalable architecture  
✅ Secure & cost-effective solution  
✅ Custom short URLs (Optional)  
✅ URL Expiration & Analytics (Optional)  

---

## 🏗 Architecture
🚀 **Frontend:** HTML & JavaScript (hosted on S3 + CloudFront)  
🖥️ **Backend:** AWS Lambda (Python)  
🗄️ **Database:** AWS DynamoDB  
🌐 **API Gateway:** RESTful API exposure  
📦 **CI/CD:** GitHub Actions for automated deployment  

![Architecture Diagram](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2022/06/09/urlshortener-diagram.png)

---

## 🛠 Tech Stack
🔹 **Frontend:** HTML, JavaScript (Fetch API, AJAX)  
🔹 **Backend:** AWS Lambda (Python)  
🔹 **Database:** AWS DynamoDB (NoSQL)  
🔹 **API:** AWS API Gateway  
🔹 **Storage:** AWS S3 (Frontend Hosting)  
🔹 **Deployment:** GitHub Actions  

---

## 🚀 Deployment Guide
### 📝 Prerequisites
- AWS Account
- AWS CLI installed & configured
- Serverless Framework or AWS SAM (optional)

### 🏗 Steps
1️⃣ Clone the repository:
```sh
git clone https://github.com/your-username/serverless-url-shortener.git
cd serverless-url-shortener
```
2️⃣ Install dependencies:
```sh
pip install -r lambda/requirements.txt -t lambda/
```
3️⃣ Deploy AWS Lambda:
```sh
cd lambda
zip -r ../lambda.zip .
aws lambda update-function-code --function-name <your-lambda-name> --zip-file fileb://../lambda.zip
```
4️⃣ Deploy Frontend to S3:
```sh
aws s3 sync frontend/ s3://url-shortener-frontend/
```

---

## 🔥 Usage
### 🌍 Shorten a URL (Frontend Example in JavaScript)
```js
async function shortenUrl() {
    const url = document.getElementById('url').value;
    const response = await fetch('https://<your-api-id>.execute-api.<region>.amazonaws.com/prod/shorten', {
        method: 'POST',
        body: JSON.stringify({ url }),
        headers: { 'Content-Type': 'application/json' }
    });
    const data = await response.json();
    document.getElementById('result').innerText = data.short_url || data.error;
}
```

### ⚡ Lambda Function (Python)
```python
import json
import boto3
import random
import string
import urllib.parse

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("UrlMappings")

def lambda_handler(event, context):
    if event["httpMethod"] == "POST":
        body = json.loads(event["body"])
        original_url = body.get("url")
        short_code = "".join(random.choices(string.ascii_letters + string.digits, k=6))
        table.put_item(Item={"short_code": short_code, "original_url": original_url})
        short_url = f"https://{event['requestContext']['domainName']}/{short_code}"
        return {"statusCode": 200, "body": json.dumps({"short_url": short_url})}
```

---

## 📌 Enhanced Features (Optional)
### ✨ Custom Short URLs
- Allow users to specify custom short codes.
- Validate uniqueness in DynamoDB.

### ⏳ URL Expiration
- Set an expiration date for shortened URLs.
- Validate expiration before redirection.

### 📊 Analytics
- Track the number of clicks on each short URL.
- Store and update click counts in DynamoDB.

---

## 📜 License
This project is open-source and available under the **MIT License**.

---

💡 **Contributions and PRs are welcome!** Feel free to enhance the project with new features or improvements. 🚀

