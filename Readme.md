# Install
```bash
sudo apt install python3
sudo apt install python3-pip
sudo apt install libssl-dev
sudo pip install pycryptodome==3.20.0
```

# Start
```bash
sudo python3 node_send_recive.py
```


# Using Docker
## Install The Docker
```bash
for pkg in docker.io docker-doc docker-compose podman-docker containerd runc; do sudo apt-get remove $pkg; done

# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/raspbian/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Set up Docker's APT repository:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/raspbian \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

## Build The Docker file
```bash
sudo docker build -t node_server .
```

## Run the Docker file 
```bash
sudo docker run --name node --privileged -t --restart always node_server 
```

## See logs:
```bash
sudo docker container logs node
```

## Inside the container:
```bash
sudo docker container exec -it node bash
```