# Flask Jenkins CI/CD Deployment Project

Designed and deployed an automated CI/CD pipeline for a Python Flask web application using GitHub, Jenkins, Docker, Docker Hub, and AWS EC2.

## Project Overview

This project demonstrates a complete DevOps deployment workflow where application code is maintained in GitHub, automatically built and containerized using Jenkins and Docker, pushed to Docker Hub, and deployed to an AWS EC2 instance.

The pipeline automates the process from source code → Docker image → Docker Hub → AWS EC2 → running application.


# Application Layer

Python Flask web application
HTML/CSS frontend
Application containerized using Docker
Application exposed on port 5000
Docker container deployed on AWS EC2


# CI/CD Pipeline

Jenkins is used to automate the complete deployment process:

Retrieves application code from GitHub
Installs Python dependencies
Verifies Flask installation
Builds the Docker image
Tags the Docker image
Pushes the image to Docker Hub
Connects to AWS EC2 through SSH
Pulls the latest Docker image
Stops and removes the previous container
Starts the updated container
Verifies the deployed container


# Technologies & Tools Used

Application
Python
Flask
HTML
CSS
DevOps & CI/CD
Git
GitHub
Jenkins
Jenkinsfile
Docker
Docker Hub
Cloud
Amazon EC2
Ubuntu Linux
Deployment & Security
SSH
SSH Key-Based Authentication
Docker Containerization


# Features Implemented

GitHub-based source code management
Jenkins CI/CD pipeline
Automated dependency installation
Flask application verification
Docker image creation
Docker Hub image publishing
Automated EC2 deployment
Passwordless Jenkins-to-EC2 SSH communication
Automatic replacement of the previous Docker container
Deployment verification through Jenkins


# CI/CD Workflow

Developer  --> GitHub  --> Jenkins  --> Checkout Source Code  --> Install Dependencies  --> Verify Flask  --> Docker Build  --> Docker Tag  --> Docker Hub  --> Jenkins  → SSH  --> AWS EC2  --> Docker Pull  --> Stop Old Container  --> Remove Old Container  --> Start New Docker Container  --> Flask Application  --> Verify Deployment


# Jenkins–EC2 Integration

Jenkins was connected to the EC2 instance using SSH key-based authentication.

The Jenkins public key was authorized on the EC2 server, allowing Jenkins to connect to EC2 automatically without requiring a password or manually providing an EC2 private key during deployment.

This enables Jenkins to perform automated deployment tasks directly on the EC2 instance.


# Docker Deployment

The Flask application is packaged as a Docker image and stored in Docker Hub.

During deployment, the EC2 instance:

Pulls the latest Docker image from Docker Hub
Stops the existing Flask container
Removes the old container
Starts a new container using the latest image
Exposes the application through port 5000


## 📁 Project Structure

Python dependencies  -->  Docker image configuration  -->  Jenkins CI/CD pipeline  -->  Project documentation  - ->  Flask HTML template  -->  Application styling

# Why I Built This Project

The main objective of this project was to gain practical experience with CI/CD, containerization, automation, and cloud deployment.

It demonstrates how multiple DevOps tools work together:

GitHub → Source code management
Jenkins → CI/CD automation
Docker → Application containerization
Docker Hub → Container image storage
SSH → Secure automated communication
AWS EC2 → Application hosting

The project shows how a code change can move from a GitHub repository to a running application on AWS through an automated deployment pipeline.


# Future Enhancements

GitHub webhook-based automatic Jenkins triggering
Docker image versioning
AWS ECR integration
Nginx reverse proxy
HTTPS/SSL configuration
CloudWatch monitoring
Application Load Balancer
Auto Scaling
Terraform-based infrastructure automation
Blue-green or rolling deployments



