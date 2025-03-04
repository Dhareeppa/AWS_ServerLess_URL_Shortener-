# ServerLess_URL_Shortener-
# Serverless URL Shortener

## 🚀 Overview
The **Serverless URL Shortener** is a highly scalable, cost-effective, and easy-to-deploy URL shortening service. Built using AWS Lambda, API Gateway, DynamoDB, and S3, it allows users to generate short URLs and track their usage without managing servers.

## 📌 Features
- 🔗 Generate short URLs instantly
- 📊 Track URL clicks and analytics
- 🏗️ Fully serverless architecture (AWS Lambda, DynamoDB, API Gateway)
- 🔒 Secure and scalable
- 📂 Custom domain support (optional)

## 🏗 Architecture
The application consists of:
- **API Gateway** – Exposes HTTP endpoints
- **Lambda Functions** – Handles URL shortening and redirection
- **DynamoDB** – Stores original and shortened URLs
- **S3 + CloudFront (Optional)** – Hosts static frontend

## 🛠️ Tech Stack
- **Backend:** AWS Lambda (Python/Node.js)
- **Database:** AWS DynamoDB (NoSQL)
- **API:** AWS API Gateway
- **Frontend (Optional):** React.js + S3 + CloudFront

## 🚀 Deployment
### Prerequisites
- AWS Account
- AWS CLI installed & configured
- Serverless Framework or AWS SAM (optional)

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/serverless-url-shortener.git
   cd serverless-url-shortener
   ```
2. Install dependencies:
   ```sh
   npm install  # or pip install -r requirements.txt (for Python)
   ```
3. Deploy to AWS:
   ```sh
   serverless deploy  # Using Serverless Framework
   ```

## 🔥 Usage
- **Shorten a URL:**
  ```sh
  curl -X POST https://your-api-gateway-url/shorten -d '{"url": "https://example.com"}'
  ```
- **Redirect using Short URL:**
  ```sh
  curl -L https://your-api-gateway-url/{short_id}
  ```

## 📜 License
This project is open-source and available under the MIT License.

---
💡 Contributions and PRs are welcome!

