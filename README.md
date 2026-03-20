# DevOps CI/CD Pipeline Project (Jenkins + SonarQube + Docker + Kubernetes)

## Project Overview

This project demonstrates a complete DevOps CI/CD pipeline for a Python application. The pipeline automates code checkout, dependency installation, unit testing, code quality analysis, Docker image creation, pushing images to Docker Hub, and deployment to a Kubernetes cluster.

The application is a simple Flask-based web service that returns a message when accessed. The project includes automated testing using pytest and static code analysis using SonarQube.

---

## Architecture

Pipeline workflow:

```
Developer → GitHub → Jenkins Pipeline
                        ↓
                 Install Dependencies
                        ↓
                     Run Tests
                        ↓
                SonarQube Code Analysis
                        ↓
                  Quality Gate Check
                        ↓
                 Build Docker Image
                        ↓
                Push Image to Docker Hub
                        ↓
                Deploy to Kubernetes
```

---

## Project Structure

```
demo-app/
 ├── app.py
 ├── requirements.txt
 ├── test_app.py
 ├── sonar-project.properties
 ├── Dockerfile
 ├── Jenkinsfile
 └── k8s
     ├── deployment.yaml
     └── service.yaml
```

---

## Application Code

### app.py

This file contains the main Flask application.

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from DevOps CI/CD Pipeline!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

The application exposes a single HTTP endpoint (`/`) that returns a message.

---

## Unit Testing

### test_app.py

This file contains unit tests for the application using pytest.

```python
from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
```

The test checks whether the application responds successfully when the root endpoint is accessed.

---

## Python Dependencies

### requirements.txt

```
flask
pytest
pytest-cov
```

These dependencies install:

* Flask (web framework)
* pytest (testing framework)
* pytest-cov (test coverage reporting)

---

## SonarQube Configuration

### sonar-project.properties

```
sonar.projectKey=demo-app
sonar.projectName=demo-app
sonar.projectVersion=1.0

sonar.sources=.
sonar.tests=.
sonar.python.coverage.reportPaths=coverage.xml
```

This configuration enables SonarQube to analyze the project source code and test coverage.

---

## Docker Configuration

### Dockerfile

```
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]
```

This Dockerfile builds a container image that runs the Flask application.

---

## Kubernetes Deployment

### deployment.yaml

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: sonar-docker-k8s

spec:
  replicas: 2
  selector:
    matchLabels:
      app: sonar-docker-k8s

  template:
    metadata:
      labels:
        app: sonar-docker-k8s

    spec:
      containers:
      - name: sonar-docker-k8s
        image: shankarduppala/sonar-docker-k8s:latest
        imagePullPolicy: Always
        ports:
        - containerPort: 5000
```

---

### service.yaml

```
apiVersion: v1
kind: Service
metadata:
  name: sonar-docker-k8s

spec:
  type: NodePort
  selector:
    app: sonar-docker-k8s

  ports:
  - port: 80
    targetPort: 5000
    nodePort: 30007
```

The service exposes the application externally through a NodePort.

---

## Jenkins Pipeline

### Jenkinsfile

The pipeline automates the build and deployment process.

Stages included in the pipeline:

1. Checkout Code
2. Install Dependencies
3. Run Unit Tests
4. SonarQube Code Analysis
5. Quality Gate Check
6. Build Docker Image
7. Push Docker Image to Docker Hub
8. Deploy to Kubernetes

---

## Running the Application Locally

Install dependencies:

```
pip install -r requirements.txt
```

Run the application:

```
python app.py
```

Access the application:

```
http://localhost:5000
```

---

## Running Tests

Execute tests using pytest:

```
pytest --cov=. --cov-report=xml
```

---

## Kubernetes Deployment

Apply Kubernetes manifests:

```
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

Check pods:

```
kubectl get pods
```

Check service:

```
kubectl get svc
```

---

## Tools Used

* Jenkins – CI/CD automation
* SonarQube – Code quality analysis
* Docker – Containerization
* Docker Hub – Image registry
* Kubernetes – Container orchestration
* Flask – Python web framework
* pytest – Testing framework

---

## Key Features

* Automated CI/CD pipeline
* Static code analysis and quality gates
* Unit testing with coverage
* Dockerized application
* Kubernetes deployment
* Dynamic image deployment

---

## Future Improvements

Possible improvements to enhance the project:

* Add container vulnerability scanning
* Implement GitOps deployment using ArgoCD
* Use Helm for Kubernetes packaging
* Add monitoring with Prometheus and Grafana
* Implement automated rollback strategies

---

## Conclusion

This project demonstrates a complete DevOps pipeline integrating continuous integration, automated testing, static code analysis, containerization, and Kubernetes-based deployment. It simulates a real-world CI/CD workflow used in modern cloud-native environments.
