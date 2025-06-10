# 🚀 CyberGuard Threat Detection System

![Hacker Theme](https://img.shields.io/badge/Theme-Hacker%20Style-green) 
![FastAPI](https://img.shields.io/badge/Framework-FastAPI-blue) 
![AWS Lambda](https://img.shields.io/badge/Deployment-AWS_Lambda-orange)

A machine learning-powered web application that detects malicious network activity in real-time, built with **FastAPI** and designed for deployment on **AWS Lambda**.

---


## 🌟 Features
- **Real-time threat detection** using a trained Random Forest model
- **Hacker-themed UI** with interactive terminal-style interface
- **Form input validation** for network session parameters
- **Responsive design** works on desktop and mobile
- **Serverless deployment** via AWS Lambda + API Gateway

## 🔧 Technologies Used
- **Backend**: Python, FastAPI, Mangum (for Lambda)
- **Frontend**: HTML5, CSS3 (hacker-themed), Jinja2 templates
- **ML**: Scikit-learn, Pandas, Pickle (model serialization)
- **Infrastructure**: AWS Lambda, API Gateway, S3 (for static files)

## 🛠️ Installation

### Local Development
1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/cyberguard.git
   cd cyberguard
Install dependencies:

bash
pip install -r requirements.txt
Run the FastAPI server:

bash
uvicorn main:app --reload
Access at: http://localhost:8000

Docker Deployment
bash
docker build -t cyberguard-app .
docker run -d -p 8000:8000 cyberguard-app
☁️ AWS Lambda Deployment
Package the app:

bash
mkdir package
pip install -r requirements.txt -t package/
cp -r main.py templates static *.pkl package/
cd package && zip -r ../cyberguard-lambda.zip .
Create Lambda function (Python 3.9+) and upload ZIP.

Set handler to main.handler.

Configure API Gateway (REST API) to trigger the Lambda.

📂 Project Structure
text
cyberguard/
├── main.py               # FastAPI application
├── requirements.txt      # Python dependencies
├── Dockerfile            # Container configuration
├── static/               # CSS/JS assets
│   ├── styles.css        # Hacker-themed styles
│   └── script.js         # Matrix animation logic
├── templates/            # Jinja2 templates
│   └── index.html        # Main interface
└── *.pkl                 # ML model and encoders
📊 Sample Input
Parameter	Example Value
Network Packet Size	1500
Protocol Type	TCP
Login Attempts	3
Session Duration	120.5
Encryption Used	TLS

👨‍💻 Author
[Vivek Chaudhari] - GitHub

Warning
The ML model is for demonstration purposes only. Not production-grade security.
