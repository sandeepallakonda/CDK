# 🚀 AWS CDK Projects — Step-by-Step from Scratch (Python)

Infrastructure as Code (IaC) is a core skill for modern **Cloud & DevOps Engineers**.

This repository contains **hands-on AWS CDK (Python) projects**, where each project explains **how to create AWS resources from absolute zero** — no assumptions, no skipped steps.

Every project focuses on:
- What the AWS service is
- Why it is required
- How to install prerequisites
- How to write CDK code
- How to deploy and destroy infrastructure safely

---

## 📌 What is AWS CDK?

**AWS Cloud Development Kit (CDK)** is an Infrastructure as Code (IaC) framework that allows you to define AWS infrastructure using programming languages like:

- Python ✅
- TypeScript
- Java
- C#
- Go

Instead of writing raw CloudFormation YAML/JSON, you write **Python code**, and CDK **synthesizes it into CloudFormation templates**.

---

## 🧰 Tech Stack Used

- **AWS CDK (Python)**
- **AWS CLI**
- **Python 3.9+**
- **Node.js (required by CDK)**
- **CloudFormation (under the hood)**

---

## 📂 Repository Structure

```bash
CDK/
│
├── ec2/                 # EC2 creation using CDK
├── vpc/                 # VPC and networking using CDK
├── lambda/              # AWS Lambda using CDK
├── s3/                  # S3 resources using CDK (if added)
├── iam/                 # IAM roles and policies
│
├── README.md            # Project documentation
└── .gitignore
````

> Each folder is an **independent CDK project** with its own code and explanation.

---

## ✅ Prerequisites

Before starting, make sure you have the following installed:

### 1️⃣ AWS Account

* An active AWS account
* Programmatic access enabled

### 2️⃣ AWS CLI

```bash
aws --version
```

Configure it:

```bash
aws configure
```

### 3️⃣ Python

```bash
python --version
```

### 4️⃣ Node.js (Required for CDK)

```bash
node --version
```

### 5️⃣ AWS CDK

```bash
npm install -g aws-cdk
cdk --version
```

---

## 🚀 Getting Started (Common for All Projects)

### Step 1: Clone the Repository

```bash
git clone https://github.com/sandeepallakonda/CDK.git
cd CDK
```

### Step 2: Navigate to a Project

```bash
cd ec2
# or
cd vpc
# or
cd lambda
```

### Step 3: Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Bootstrap CDK (First Time Only)

```bash
cdk bootstrap
```

---

## 📦 Deploying the Stack

```bash
cdk synth     # Generates CloudFormation template
cdk deploy    # Deploys resources to AWS
```

After deployment, verify resources in:

* AWS EC2 Console
* VPC Console
* Lambda Console
* CloudFormation Console

---

## 🧹 Destroying Resources (Important)

Always clean up resources to avoid unwanted AWS charges:

```bash
cdk destroy
```

---

## 📘 Projects Included

### 🔹 EC2 Using AWS CDK

* Create EC2 instance from scratch
* Key pairs & security groups
* AMI selection
* Instance type configuration

### 🔹 VPC Using AWS CDK

* Custom VPC
* Public & private subnets
* Internet Gateway
* Route tables

### 🔹 AWS Lambda Using CDK

* Lambda function creation
* IAM permissions
* Environment variables
* Testing deployment

> More CDK projects will be added continuously.

---

## 📖 Blogs & Learning Resources

* **Medium Blog:**
  [https://medium.com/@sandeepallakonda](https://medium.com/@sandeepallakonda)

* **GitHub Repository:**
  [https://github.com/sandeepallakonda/CDK](https://github.com/sandeepallakonda/CDK)

---

## 🎯 Who Is This Repository For?

* Beginners learning AWS CDK
* DevOps Engineers
* Cloud Engineers
* Students preparing for AWS interviews
* Anyone moving from manual AWS to Infrastructure as Code

---

## 🤝 Contributions

Contributions are welcome!

* Fork the repo
* Create a feature branch
* Raise a Pull Request

---

## ⭐ Support

If you find this repository useful:

* ⭐ Star the repo
* 🍴 Fork it
* 🔄 Share it with the community

---

## 👨‍💻 Author

**Sandeep Allakonda**
DevOps | AWS | Cloud Infrastructure
GitHub: [https://github.com/sandeepallakonda](https://github.com/sandeepallakonda)
Medium: [https://medium.com/@sandeepallakonda](https://medium.com/@sandeepallakonda)

---

Happy Learning & Building with AWS CDK 🚀

```
