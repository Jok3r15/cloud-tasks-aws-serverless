# CloudTasks - AWS Serverless Task Manager

A professional, full-stack serverless web application built on **Amazon Web Services (AWS)**. This project demonstrates a secure cloud architecture focused on scalability, user identity management, and cost-efficient infrastructure.

## 🚀 Key Features
- **Secure Authentication:** Full user lifecycle (Signup, Login, Verification, and Password Recovery) powered by **AWS Cognito** (JWT).
- **Multilingual UI:** Support for English and Spanish with persistent user preference and password visibility toggle.
- **Serverless API:** A scalable RESTful API built with **Amazon API Gateway** and **AWS Lambda** (Python).
- **NoSQL Persistence:** High-performance data storage with **Amazon DynamoDB**, featuring user-based data isolation.
- **Cloud Monitoring:** Infrastructure health alerts via **CloudWatch** and **SNS** (Simple Notification Service).
- **FinOps Ready:** Automated **AWS Budgets** alerts to ensure cost control.

## 🛠️ Technology Stack
- **Frontend:** HTML5, Tailwind CSS, JavaScript (Vanilla), Cognito Identity SDK.
- **Backend:** AWS Lambda (Python 3.9), Boto3.
- **Database:** Amazon DynamoDB (NoSQL).
- **Hosting & Infrastructure:** Amazon S3, API Gateway, CloudWatch, SNS, AWS Budgets.

## 📐 Architecture Overview
The application follows a modern serverless event-driven architecture. 



1. **Frontend:** Single-page application (SPA) hosted on S3.
2. **Identity:** API requests are authorized via Cognito User Pool tokens to ensure data privacy.
3. **Compute:** Python-based Lambda functions handle CRUD operations for tasks.
4. **Storage:** DynamoDB uses `userId` as the partition key to guarantee that users only access their own data.
5. **Observability:** CloudWatch monitors for errors and triggers email notifications via SNS.

## 📄 License
This project is licensed under the MIT License.
