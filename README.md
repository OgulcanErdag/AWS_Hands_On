# ☁️ AWS Hands-On Practices

This repository includes structured **AWS hands-on exercises** created to strengthen practical knowledge of core AWS services.  
Each folder represents a separate topic-based lab focusing purely on **hands-on implementation** — not theory, slides, or documentation.

---

## 🎯 Purpose

The repository is dedicated exclusively to **hands-on practice**.  
It is not a note collection or lecture summary, but a technical workspace for:

- Practicing real AWS commands and configurations
- Reproducing common AWS architecture scenarios
- Testing automation scripts and CloudFormation templates
- Building repeatable infrastructure examples

---

## 🧩 Repository Structure

Each folder corresponds to a hands-on exercise:

EC2_Introduction
📁 IAM
📁 NGINX-Launch_Template
📁 Volumes
📁 AMI_Snapshot
📁 Guile-ELB
📁 Load_Balancing
📁 Auto_Scaling
📁 CFN-ASG-ALB-LT
📁 EFS
📁 Guile-CFN-ASG-ALB-LT
📁 S3_1
📁 S3_02
📁 Guile-CLI
📁 Database_RDS
📁 Guile-MariaDB
📁 DB_Restore_SS_PiT
📁 Guile-DynamoDB
📁 VPC_01
📁 Guile-VPC-2
📁 VPC-3
📁 Cloudwatch
📁 Route_53_1
📁 Route_53_2
📁 VPC_04
📁 Guile-CloudFront
📁 Guile-Lambda-APIGW
📁 Elastic_Beanstalk
📁 Guile-SNS-SQS
📁 Boto3
📁 Cloud_Formation_Sample
📁 Cloud_Front
📁 DynamoDB
📁 JSON_YAML
📁 Lambda_API

Each folder contains:

- `guide.md` or `README.md` → step-by-step exercise instructions
- `user_data.sh`, `.yaml`, or `.json` → configuration or automation files
- `screenshots/` → validation and output images

---

## 🧠 Topics Covered

| Category         | Example Hands-On Topics                                       |
| ---------------- | ------------------------------------------------------------- |
| 🖥️ EC2           | Launching instances, connecting via SSH, user data automation |
| 🔐 IAM           | User, group, and policy management                            |
| ☁️ S3            | Static website hosting, lifecycle rules, encryption           |
| 🧱 EFS & Volumes | Mounting, sharing, and performance tuning                     |
| 🧮 Databases     | RDS, MariaDB, DynamoDB, backups                               |
| 🌐 Networking    | VPC, Subnets, Route Tables, NAT, Load Balancers               |
| 📊 Monitoring    | CloudWatch metrics, alarms, logs                              |
| ⚙️ Automation    | CloudFormation, Bash scripting, Boto3                         |
| 🪄 Serverless    | Lambda, API Gateway, SNS, SQS                                 |
| 🚀 Deployment    | Elastic Beanstalk, Auto Scaling, Launch Templates             |

---

## 📁 Example Folder Format

Each hands-on includes:

1. **Objective** – What will be implemented
2. **Implementation Steps** – Commands and configurations
3. **Verification** – How to test the setup
4. **Cleanup** – Optional removal of test resources

---

## 🧾 Progress Overview

| No  | Topic                  | Folder                                             |
| --- | ---------------------- | -------------------------------------------------- | --- |
| 01  | EC2 Introduction       | [EC2_Introduction](./EC2_Introduction)             |
| 02  | IAM                    | [IAM](./IAM)                                       |
| 03  | NGINX Launch Template  | [NGINX-Launch_Template](./NGINX-Launch_Template)   |     |
| 04  | Volumes                | [Volumes](./Volumes)                               |
| 05  | AMI & Snapshot         | [AMI_Snapshot](./AMI_Snapshot)                     |
| 06  | ELB                    | [Guile-ELB](./Guile-ELB)                           |
| 07  | Load Balancing         | [Load_Balancing](./Load_Balancing)                 |
| 08  | Auto Scaling           | [Auto_Scaling](./Auto_Scaling)                     |
| 09  | CFN ASG ALB LT         | [CFN-ASG-ALB-LT](./CFN-ASG-ALB-LT)                 |
| 10  | EFS                    | [EFS](./EFS)                                       |
| 11  | CFN ASG ALB LT (Guile) | [Guile-CFN-ASG-ALB-LT](./Guile-CFN-ASG-ALB-LT)     |
| 12  | S3 - Part 1            | [S3_1](./S3_1)                                     |
| 13  | S3 - Part 2            | [S3_02](./S3_02)                                   |
| 14  | AWS CLI                | [Guile-CLI](./Guile-CLI)                           |
| 15  | Database RDS           | [Database_RDS](./Database_RDS)                     |
| 16  | MariaDB                | [Guile-MariaDB](./Guile-MariaDB)                   |
| 17  | DB Restore SS PiT      | [DB_Restore_SS_PiT](./DB_Restore_SS_PiT)           |
| 18  | DynamoDB               | [Guile-DynamoDB](./Guile-DynamoDB)                 |
| 19  | VPC - Part 1           | [VPC_01](./VPC_01)                                 |
| 20  | VPC - Part 2           | [Guile-VPC-2](./Guile-VPC-2)                       |
| 21  | VPC - Part 3           | [VPC-3](./VPC-3)                                   |
| 22  | CloudWatch             | [Cloudwatch](./Cloudwatch)                         |
| 23  | Route 53 - Part 1      | [Route_53_1](./Route_53_1)                         |
| 24  | Route 53 - Part 2      | [Route_53_2](./Route_53_2)                         |
| 25  | VPC - Part 4           | [VPC_04](./VPC_04)                                 |
| 26  | CloudFront             | [Guile-CloudFront](./Guile-CloudFront)             |
| 27  | Lambda & API Gateway   | [Guile-Lambda-APIGW](./Guile-Lambda-APIGW)         |
| 28  | Elastic Beanstalk      | [Elastic_Beanstalk](./Elastic_Beanstalk)           |
| 29  | SNS & SQS              | [Guile-SNS-SQS](./Guile-SNS-SQS)                   |
| 30  | Boto3                  | [Boto3](./Boto3)                                   |
| 31  | CloudFormation Sample  | [Cloud_Formation_Sample](./Cloud_Formation_Sample) |
| 32  | CloudFront             | [Cloud_Front](./Cloud_Front)                       |
| 33  | DynamoDB               | [DynamoDB](./DynamoDB)                             |
| 34  | JSON & YAML            | [JSON_YAML](./JSON_YAML)                           |
| 35  | Lambda & API           | [Lambda_API](./Lambda_API)                         |

---

## ⚙️ Tools & Environment

- **AWS Management Console & CLI**
- **Amazon Linux 2 / 2023**
- **Bash, YAML, JSON**
- **VS Code + Git**
- **Free Tier AWS Environment**

---

## 📌 Notes

- Only hands-on practice content is included — **no lecture notes or slides**.
- All labs are designed to run safely under the **AWS Free Tier**.
- Access keys and credentials are **never uploaded**.

---

> “Hands-on is the fastest way to understand the cloud.”  
> _Every folder here represents a real practice lab._

---
