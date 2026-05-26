# CloudTasks - AWS Serverless Task Manager

A professional, full-stack serverless web application built on Amazon Web Services (AWS). This project demonstrates a secure cloud architecture focused on scalability, user identity management, and cost-efficient infrastructure.

---

## 🚀 Key Features

* **Secure Authentication:** Full user lifecycle (Signup, Login, Verification, and Password Recovery) powered by AWS Cognito (JWT).
* **Multilingual UI:** Support for English and Spanish with persistent user preference and password visibility toggle.
* **Serverless API:** A scalable RESTful API built with Amazon API Gateway and AWS Lambda (Python).
* **NoSQL Persistence:** High-performance data storage with Amazon DynamoDB, featuring user-based data isolation.
* **Cloud Monitoring:** Infrastructure health alerts via CloudWatch and SNS (Simple Notification Service).
* **FinOps Ready:** Automated AWS Budgets alerts to ensure cost control.

---

## 📐 Architecture Overview

The application follows a modern serverless event-driven architecture designed to maximize operational excellence and minimize maintenance overhead.

* **Frontend:** Single-page application (SPA) hosted on Amazon S3.
* **Identity:** API requests are authorized via Cognito User Pool tokens to ensure data privacy and secure session handling.
* **Compute:** Python-based Lambda functions handle CRUD operations for tasks, built in a modular architecture.
* **Storage:** DynamoDB uses `userId` as the partition key to guarantee that users only access their own data.
* **Observability:** CloudWatch monitors for errors and triggers email notifications via SNS.

---

## 🧠 Architectural Decisions & Security Patterns

To meet enterprise engineering standards, the following technical patterns were implemented in this infrastructure:

* **Infrastructure as Code (IaC):** Defined entirely via AWS SAM (`template.yaml`), allowing reproducible, consistent, and version-controlled environment deployments, eliminating configuration drift.
* **Data Isolation:** Implements strict user-based multi-tenancy isolation in DynamoDB by using the Cognito unique `sub` (User ID) as the Partition Key.
* **Principle of Least Privilege:** Lambda execution IAM Roles are tightly locked down to the exact actions needed to read/write to the specific DynamoDB table, preventing unauthorized lateral movement.
* **Production-Ready Code:** Python backend functions feature structured `try/except` exception handling and logging to prevent unhandled 500 server errors and ensure clear Root Cause Analysis (RCA).

---

## 🛠️ Technology Stack

* **Frontend:** HTML5, Tailwind CSS, JavaScript (Vanilla), Cognito Identity SDK.
* **Backend:** AWS Lambda (Python 3.9), Boto3.
* **Database:** Amazon DynamoDB (NoSQL).
* **Hosting & Infrastructure:** Amazon S3, API Gateway, CloudWatch, SNS, AWS Budgets.
* **Deployment Tooling:** AWS SAM CLI (Serverless Application Model) / CloudFormation.

---

## 🚀 Deployment & Local Development

This project uses the AWS SAM CLI for building and deployment.

### Prerequisites
* AWS CLI configured with appropriate IAM permissions.
* AWS SAM CLI installed.
* Python 3.9 or higher.

### Build the application
```bash
sam build
