# Flask + PostgreSQL DevOps Project

A complete DevOps stack:
- Flask backend
- PostgreSQL database
- Docker Compose for development
- Kubernetes manifests for cloud deployment
- Terraform for AWS provisioning
- GitHub Actions for CI

## Run Locally
```bash
docker-compose up --build
```

## Kubernetes Deployment
```bash
kubectl apply -f k8s/postgres.yaml
kubectl apply -f k8s/deployment.yaml
```

## Terraform AWS EC2
```bash
cd infra
terraform init
terraform apply
```

## CI/CD
GitHub Actions workflow runs on push.
