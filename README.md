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