# Serverless URL Shortener

## 🚀 Overview
The **Serverless URL Shortener** is a highly scalable, cost-effective, and easy-to-deploy URL shortening service. Built using AWS Lambda, API Gateway, DynamoDB, and S3, it allows users to generate short URLs and track their usage without managing servers.

## 📌 Features
- 🔗 Generate short URLs instantly
- 📊 Track URL clicks and analytics
- 🏗️ Fully serverless architecture (AWS Lambda, DynamoDB, API Gateway, S3)
- 🔒 Secure and scalable
- 📂 Custom domain support (optional)

## 🏗 Architecture
The application consists of:
- **API Gateway** – Exposes HTTP endpoints
- **Lambda Functions (Python)** – Handles URL shortening and redirection
- **DynamoDB** – Stores original and shortened URLs
- **S3 + CloudFront** – Hosts static frontend (HTML, JavaScript, CSS)

## 🛠️ Tech Stack
- **Frontend:** HTML, JavaScript (AJAX, Fetch API)
- **Backend:** AWS Lambda (Python)
- **Database:** AWS DynamoDB (NoSQL)
- **API:** AWS API Gateway
- **Storage:** AWS S3 (Frontend Hosting)

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
   pip install -r requirements.txt
   ```
3. Deploy to AWS:
   ```sh
   serverless deploy  # Using Serverless Framework
   ```
4. Upload frontend files (HTML, JS, CSS) to S3:
   ```sh
   aws s3 sync frontend/ s3://your-bucket-name --acl public-read
   ```

## 🔥 Usage
- **Shorten a URL (Frontend Example in JavaScript):**
  ```js
  fetch('https://your-api-gateway-url/shorten', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ url: 'https://example.com' })
  })
  .then(response => response.json())
  .then(data => console.log('Short URL:', data.shortUrl));
  ```

- **Redirect using Short URL:**
  ```sh
  curl -L https://your-api-gateway-url/{short_id}
  ```

## 📜 License
This project is open-source and available under the MIT License.

---
💡 Contributions and PRs are welcome!

