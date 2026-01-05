# 🔐 Network Security ML Pipeline

## 📌 Overview
This project is an **end-to-end, production-grade Machine Learning pipeline** for a **network security use case**, designed with real-world **MLOps practices**. It covers everything from data ingestion to model training and automated deployment on AWS using CI/CD.

The goal of this project is to demonstrate how ML systems are built, versioned, deployed, and maintained in production — not just how models are trained.

---

## 🧠 Problem Statement
Traditional ML projects often stop at model training and lack:
- Automation
- Versioning
- Deployment
- Monitoring readiness

This project solves that by implementing a **fully modular and automated ML pipeline** that:
- Ingests and validates data
- Transforms features
- Trains and evaluates models
- Stores artifacts and models in AWS S3
- Deploys the application using Docker, EC2, and GitHub Actions

---

## 🏗 Architecture
**High-level flow:**

Data Source → Data Ingestion → Data Validation → Data Transformation → Model Training

⬇️

Artifacts & Trained Model → AWS S3 (versioned by timestamp)

⬇️

FastAPI Application → Docker → AWS ECR → AWS EC2

⬇️

Automated via GitHub Actions (CI/CD)

📌 *Refer to the architecture diagram attached in the repository.*

---

## 🛠 Tech Stack
- **Language:** Python
- **ML:** Scikit-learn
- **API:** FastAPI
- **Containerization:** Docker
- **Cloud:** AWS (EC2, S3, ECR, IAM)
- **CI/CD:** GitHub Actions
- **Logging & Exceptions:** Custom logging and exception handling

---


## ⚙️ Pipeline Components

### 1️⃣ Data Ingestion
- Fetches raw data
- Splits data into training and testing sets
- Stores ingestion artifacts

### 2️⃣ Data Validation
- Schema validation
- Data drift checks
- Ensures data quality before training

### 3️⃣ Data Transformation
- Feature engineering
- Encoding and scaling
- Saves transformation objects

### 4️⃣ Model Trainer
- Trains ML models
- Evaluates performance
- Saves final trained model

---

## 📦 Artifact & Model Versioning
- All pipeline outputs are stored locally as artifacts
- Artifacts and final models are **synced to AWS S3**
- Each run is versioned using a **timestamp-based folder structure**

Example:
```
s3://<bucket-name>/artifact/<timestamp>/
s3://<bucket-name>/final_model/<timestamp>/
```

---

## 🚀 CI/CD Pipeline (GitHub Actions)
On every push to the `main` branch:
1. Code is checked out
2. Docker image is built
3. Image is pushed to AWS ECR
4. EC2 pulls the latest image
5. Container is restarted with the new version

This ensures **fully automated deployment** with no manual intervention.

---

## 🌐 Application
- Built using **FastAPI**
- Provides endpoints to trigger model training
- API documentation available via Swagger (`/docs`)

📌 The application runs inside a Docker container on AWS EC2.

---

## 🎥 Demo
A complete working demo is available as a video showing:
- Project walkthrough
- CI/CD pipeline execution
- EC2 deployment
- Model training execution
- Artifact & model uploads to S3

▶️ **Demo Video:** <Add your video link here>

> Note: The EC2 instance is intentionally stopped when not in use to optimize cloud costs.

---


## 👤 Author
**Arman Singh**  
Aspiring ML / MLOps Engineer

🔗 LinkedIn: <[https://www.linkedin.com/in/arman-singh-198343363/]>  
🐙 GitHub: <[https://github.com/Armanix-01]>
