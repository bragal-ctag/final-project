# final-project

### Reporte de test local
`pytest --cov=app --cov-report=term --cov-report=html --cov-report=xml unit_test/`

### Star minikube
`minikube start --driver=docker --cpus=4 --memory=4096`

### Get the pods status on environment
`kubectl get pods -n dev`

### Redirect Dev app ports
`kubectl port-forward svc/dev-calculadora-service 81:5000 -n dev`

### Redirect staging app ports
`kubectl port-forward svc/staging-calculadora-service 82:5000 -n staging`

### Redirect prod app ports
`kubectl port-forward svc/prod-calculadora-service 80:5000 -n prod`

### Check test DDBB content
`psql -U calc -d calculadora`
`\l`
`\dt`
`SELECT * FROM operations;`

### SonarQube
Password must be update first time and a token shall be configured as secret

### Check the pods running on the environment
`kubectl get pods -n prod`

### List the services on the cluster
`minikube service list -n prod`

### Access prometheus service
`minikube service prod-prometheus -n prod`

### Access grafana service
`minikube service prod-grafana -n prod`

### Grafana default user-password
`admin`
`admin`
