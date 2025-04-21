# My Python Project

A simple Python application with CI/CD pipeline implementation.

## Components

- Python application with a simple add_numbers function
- Unit tests with PyUnit (unittest)
- Linting with Pylint
- Docker containerization
- GitHub Actions for CI/CD
- Kubernetes deployment configuration

## Setup and Usage

### Local Development

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run tests: `python -m unittest test_app.py`
4. Run linting: `pylint app.py`
5. Run the application: `python app.py`

### Docker

```bash
# Build Docker image
docker build -t myapp .

# Run Docker container
docker run -p 5000:5000 myapp

# Push to DockerHub
docker login
docker tag myapp username/myapp:latest
docker push username/myapp:latest
```

### Kubernetes Deployment

```bash
# Apply deployment
kubectl apply -f deployment.yaml

# Expose service
kubectl expose deployment myapp-deployment --type=LoadBalancer --port=80 --target-port=5000

# Check status
kubectl get pods
kubectl get svc
```
