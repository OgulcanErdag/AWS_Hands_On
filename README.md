![AWS Log](./aws.webp)

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

📁EC2_Introduction
📁 IAM
📁 NGINX-Launch_Template
📁 Volumes
📁 AMI_Snapshot
📁 JSON_YAML
📁 Load_Balancing
📁 S3_1
📁 CFN-ASG-ALB-LT
📁 S3_2
📁 Auto_Scaling
📁 EFS
📁 CLI
📁 Database_RDS
📁 MariaDB
📁 DB_Restore_SS_PiT
📁 DynamoDB
📁 VPC_1
📁 VPC_2
📁 VPC_3
📁 Cloudwatch
📁 Route_53_1
📁 Route_53_2
📁 VPC_4
📁 CloudFront
📁 Lambda-APIGW
📁 Elastic_Beanstalk
📁 SNS-SQS
📁 Boto3
📁 Cloud_Formation_Sample
📁 Cloud_Front
📁 DynamoDB
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

| No  | Topic                 | Folder                                             |
| --- | --------------------- | -------------------------------------------------- |
| 01  | EC2 Introduction      | [EC2_Introduction](./EC2_Introduction)             |
| 02  | IAM                   | [IAM](./IAM)                                       |
| 03  | NGINX Launch Template | [NGINX-Launch_Template](./NGINX-Launch_Template)   |
| 04  | Volumes               | [Volumes](./Volumes)                               |
| 05  | AMI & Snapshot        | [AMI_Snapshot](./AMI_Snapshot)                     |
| 06  | JSON & YAML           | [JSON_YAML](./JSON_YAML)                           |
| 07  | Load Balancing        | [Load_Balancing](./Load_Balancing)                 |
| 08  | S3 - Part 1           | [S3_1](./S3_1)                                     |
| 09  | ASG-LT                | [ASG-LT](./ASG-LT)                                 |
| 10  | Auto Scaling          | [Auto_Scaling](./Auto_Scaling)                     |
| 11  | EFS                   | [EFS](./EFS)                                       |
| 12  | S3 - Part 2           | [S3_2](./S3_2)                                     |
| 13  | AWS CLI               | [CLI](./CLI)                                       |
| 14  | Database RDS          | [Database_RDS](./Database_RDS)                     |
| 15  | MariaDB               | [MariaDB](./MariaDB)                               |
| 16  | DB Restore SS PiT     | [DB_Restore_SS_PiT](./DB_Restore_SS_PiT)           |
| 17  | DynamoDB              | [DynamoDB](./DynamoDB)                             |
| 18  | VPC - Part 1          | [VPC_1](./VPC_1)                                   |
| 19  | VPC - Part 2          | [VPC-2](./VPC_2)                                   |
| 20  | VPC - Part 3          | [VPC-3](./VPC_3)                                   |
| 21  | CloudWatch            | [Cloudwatch](./Cloudwatch)                         |
| 22  | Route 53 - Part 1     | [Route_53_1](./Route_53_1)                         |
| 23  | Route 53 - Part 2     | [Route_53_2](./Route_53_2)                         |
| 24  | VPC - Part 4          | [VPC_4](./VPC_4)                                   |
| 25  | CloudFront            | [CloudFront](./CloudFront)                         |
| 26  | Lambda & API Gateway  | [Lambda-APIGW](./Lambda-APIGW)                     |
| 27  | Elastic Beanstalk     | [Elastic_Beanstalk](./Elastic_Beanstalk)           |
| 28  | SNS & SQS             | [SNS-SQS](./SNS-SQS)                               |
| 29  | Boto3                 | [Boto3](./Boto3)                                   |
| 30  | CloudFormation Sample | [Cloud_Formation_Sample](./Cloud_Formation_Sample) |
| 31  | CloudFront            | [Cloud_Front](./Cloud_Front)                       |
| 32  | DynamoDB              | [DynamoDB](./DynamoDB)                             |
| 33  | JSON & YAML           | [JSON_YAML](./JSON_YAML)                           |
| 34  | Lambda & API          | [Lambda_API](./Lambda_API)                         |

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
