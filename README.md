# final-project

### Reporte de test local
`pytest --cov=app --cov-report=term --cov-report=html --cov-report=xml unit_test/`

### Star minikube
`minikube start --driver=docker --cpus=4 --memory=4096`

### Get the pods status on environment
`kubectl get pods -n dev`

### Redirect Dev app ports
`kubectl port-forward svc/dev-calculadora-service 80:5000 -n dev`

### Redirect staging app ports
`kubectl port-forward svc/stagin-calculadora-service 80:5000 -n staging`

### Check test DDBB content
`psql -U calc -d calculadora`
`\l`
`\dt`
`SELECT * FROM operations;`

### SonarQube
Password must be update first time and a token shall be configured as secret

