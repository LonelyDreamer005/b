## Docker Commands

### 1. Build Docker Image
```bash
docker build -t bir .
```

### 2. List Docker Images
```bash
docker images
```

### 3. List All Containers
```bash
docker ps -a
```

### 4. Run Docker Container
```bash
docker run -d -p 5000:5000 --name bir-container bir:latest
```

### 5. Check Running Containers
```bash
docker ps
```

### 6. Check All Containers
```bash
docker ps -a
```

### 7. Stop Container
```bash
docker stop bir-container
```

### 8. View Container Logs
```bash
docker logs bir-container
```

### Terraform codespaces:
```bash
# Update packages
sudo apt-get update

# Install required packages
sudo apt-get install -y gnupg software-properties-common curl wget

# Add HashiCorp GPG key
wget -O- https://apt.releases.hashicorp.com/gpg | \
sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg

# Add Terraform repository
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(. /etc/os-release && echo $VERSION_CODENAME) main" | \
sudo tee /etc/apt/sources.list.d/hashicorp.list

# Update package list
sudo apt-get update

# Install Terraform
sudo apt-get install -y terraform

# Verify installation
terraform -version
```

## Kubernetes Setup and Commands

### 1. Start Minikube

```bash
minikube start --driver=docker
```

### 2. Check Minikube Status

```bash
minikube status
```

### 3. Check Kubernetes Nodes

```bash
kubectl get nodes
```

### 4. Create Deployment

Create a `k8s` directory:

```bash
mkdir k8s
```

Create `k8s/deployment.yaml`:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: bir-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: bir
  template:
    metadata:
      labels:
        app: bir
    spec:
      containers:
        - name: bir-container
          image: bir:latest
          imagePullPolicy: IfNotPresent
          ports:
            - containerPort: 5000
```

### 5. Create Service

Create `k8s/service.yaml`:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: bir-service
spec:
  type: NodePort
  selector:
    app: bir
  ports:
    - port: 5000
      targetPort: 5000
      nodePort: 30080
```

### 6. Apply Kubernetes Configuration

```bash
kubectl apply -f k8s/
```

### 7. Check Deployments

```bash
kubectl get deployments
```

### 8. Check Pods

```bash
kubectl get pods
```

### 9. Check Services

```bash
kubectl get services
```

### 10. Describe Pod

```bash
kubectl describe pod <pod-name>
```

### 11. View Pod Logs

```bash
kubectl logs <pod-name>
```

### 12. Access Application

```bash
kubectl port-forward service/bir-service 5000:5000 --address 0.0.0.0
```

Open port `5000` in the Codespaces Ports tab.

### 13. Delete Deployment

```bash
kubectl delete deployment bir-app
```

### 14. Delete Service

```bash
kubectl delete service bir-service
```

### 15. Stop Minikube

```bash
minikube stop
```

### 16. Delete Minikube Cluster

```bash
minikube delete
```

**Note:** Since the Docker image is built locally, Minikube must be able to access it. If the pod shows `ImagePullBackOff`, load the image:

```bash
minikube image load bir:latest
```

Then restart the deployment:

```bash
kubectl rollout restart deployment/bir-app
```