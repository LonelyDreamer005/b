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