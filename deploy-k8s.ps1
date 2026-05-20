docker pull 082319703213.dkr.ecr.us-east-1.amazonaws.com/backend-app:latest

docker pull 082319703213.dkr.ecr.us-east-1.amazonaws.com/frontend-app:latest

kubectl rollout restart deployment backend-deployment

kubectl rollout restart deployment frontend-deployment