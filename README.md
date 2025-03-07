### **🚀 AWS Serverless URL Shortener**  

![AWS Serverless](https://img.shields.io/badge/AWS-Serverless-orange) ![Python](https://img.shields.io/badge/Python-3.x-blue) ![License](https://img.shields.io/badge/License-MIT-green)  

A fully **serverless URL shortener** built using **AWS Lambda, DynamoDB, API Gateway, and S3**. This project allows users to shorten long URLs, store them in DynamoDB, and access them via an API. The frontend is hosted on S3 and served through CloudFront for **fast performance**.  

---

## **📌 Features**  
✅ **Shorten long URLs instantly**  
✅ **Redirect users using short URLs**  
✅ **Serverless & auto-scalable architecture**  
✅ **Secure & cost-effective solution**  
✅ **Custom short URLs (Optional)**  
✅ **URL Expiration & Analytics (Optional)**  

---

## **🏗 Architecture**  

🚀 **Frontend:** HTML & JavaScript (hosted on S3 + CloudFront)  
🖥️ **Backend:** AWS Lambda (Python)  
🗄️ **Database:** AWS DynamoDB  
🌐 **API Gateway:** RESTful API exposure  
📦 **CI/CD:** GitHub Actions for automated deployment 
![Serverless Architecture](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2022/06/09/urlshortener-diagram.png)


### **📌 How It Works:**  
1️⃣ **User submits a long URL** via the frontend.  
2️⃣ **Frontend calls the API Gateway**, which triggers the **Lambda function**.  
3️⃣ **Lambda generates a short code**, stores the mapping in **DynamoDB**, and returns the shortened URL.  
4️⃣ When a user visits the **shortened URL**, API Gateway **redirects them** to the **original URL**.  

---

## **🛠 Tech Stack**  
🔹 **Frontend:** HTML, JavaScript (Fetch API, AJAX)  
🔹 **Backend:** AWS Lambda (Python)  
🔹 **Database:** AWS DynamoDB (NoSQL)  
🔹 **API:** AWS API Gateway  
🔹 **Storage:** AWS S3 (Frontend Hosting)  
🔹 **CDN:** AWS CloudFront  
🔹 **Deployment:** GitHub Actions  

---

## **🚀 Deployment Guide**  

### **📝 Prerequisites**  
- ✅ AWS Account  
- ✅ AWS CLI installed & configured  
- ✅ Serverless Framework or AWS SAM (optional)  
- ✅ GitHub Actions set up for CI/CD  

---

### **🏗 Steps to Deploy**  

#### **1️⃣ Clone the Repository**  
```sh
git clone https://github.com/your-username/serverless-url-shortener.git
cd serverless-url-shortener
```

#### **2️⃣ Install Dependencies**  
```sh
pip install -r lambda/requirements.txt -t lambda/
```

#### **3️⃣ Deploy the Lambda Function**  
```sh
cd lambda
zip -r ../lambda.zip .
aws lambda update-function-code --function-name <your-lambda-name> --zip-file fileb://../lambda.zip
```

#### **4️⃣ Deploy the Frontend to S3**  
```sh
aws s3 sync frontend/ s3://url-shortener-frontend/ --delete
```

---

## **🌐 API Endpoints**  

| **Method** | **Endpoint**                        | **Description**                      |
|------------|------------------------------------|--------------------------------------|
| **POST**   | `/shorten`                         | Shortens a given long URL            |
| **GET**    | `/{short_code}`                    | Redirects to the original URL        |
| **GET**    | `/analytics/{short_code}` (Optional) | Fetches analytics for a short URL    |

---

## **🔥 Usage**  

### **🌍 Shorten a URL (Frontend Example in JavaScript)**  
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

### **⚡ Lambda Function (Python)**
```python
import json
import boto3
import random
import string

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("UrlMappings")

def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def lambda_handler(event, context):
    if event["httpMethod"] == "POST":
        body = json.loads(event["body"])
        original_url = body.get("url")
        short_code = generate_short_code()
        table.put_item(Item={"short_code": short_code, "original_url": original_url})
        short_url = f"https://{event['requestContext']['domainName']}/{short_code}"
        return {"statusCode": 200, "body": json.dumps({"short_url": short_url})}
```

---

## **📌 Enhanced Features (Optional)**  

### **✨ Custom Short URLs**  
- Allow users to specify **custom short codes**.  
- Validate uniqueness before storing in DynamoDB.  

### **⏳ URL Expiration**  
- Add an **expiration date** to each URL.  
- Validate expiration before redirecting users.  

### **📊 Analytics**  
- Track **clicks** on short URLs.  
- Store and update **click counts** in DynamoDB.  

---

## **🔄 CI/CD with GitHub Actions**  
### **GitHub Actions Workflow (Deploy Lambda & Frontend)**
```yaml
name: Deploy URL Shortener

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'

      - name: Install Dependencies
        run: pip install -r lambda/requirements.txt -t lambda/

      - name: Configure AWS Credentials
        uses: aws-actions/configure-aws-credentials@v2
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: us-east-1 # Change if needed

      - name: Deploy Lambda Function
        run: |
          cd lambda
          zip -r ../lambda.zip .
          cd ..
          aws lambda update-function-code --function-name your-lambda-name --zip-file fileb://lambda.zip

      - name: Deploy Frontend to S3
        run: aws s3 sync frontend/ s3://url-shortener-frontend/ --delete
```

---

## **📜 License**  
This project is **open-source** and available under the **MIT License**.  

---

💡 **Contributions & PRs are welcome!** Feel free to enhance the project with new features or improvements. 🚀  

---
