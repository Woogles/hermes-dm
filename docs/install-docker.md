Install using the apt repository

Before you install Docker Engine for the first time on a new host machine, you need to set up the Docker apt repository. Afterward, you can install and update Docker from the repository.

```bash
# Add Docker's official GPG key:
sudo apt update
sudo apt install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
sudo tee /etc/apt/sources.list.d/docker.sources <<EOF
Types: deb
URIs: https://download.docker.com/linux/ubuntu
Suites: $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}")
Components: stable
Architectures: $(dpkg --print-architecture)
Signed-By: /etc/apt/keyrings/docker.asc
EOF

sudo apt update
```

Install the Docker packages.

```bash
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin.
```

Verify that the installation is successful by running the hello-world image:
```bash
which docker
# it should respond with /usr/bin/docker
sudo systemctl status docker
# it should respond with 
# docker.service - Docker Application Container Engine
#    Loaded: loaded (/usr/lib/systemd/system/docker.service; enabled; preset: enabled)
#   Active: active (running) since Fri 2026-11-20 15:09:34 EST; 5min ago
# Invocation: 3e4c84a14a9c491c975e3fac1de1e637
# TriggeredBy: ● docker.socket
#       Docs: https://docs.docker.com
#   Main PID: 69306 (dockerd)
#      Tasks: 17
#     Memory: 36.8M (peak: 38.6M)
#        CPU: 694ms
#     CGroup: /system.slice/docker.service
#             └─69306 /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock

sudo docker run hello-world
# it should respond with 
#Unable to find image 'hello-world:latest' locally
#latest: Pulling from library/hello-world
#4f55086f7dd0: Pull complete
#d5e71e642bf5: Download complete
#Digest: sha256:1e4c05b897a751332ce85c7e9449da2d93514ea2dea6dbb0e2753c9e949b2bfa
#Status: Downloaded newer image for hello-world:latest

#Hello from Docker!
#This message shows that your installation appears to be working correctly.

#To generate this message, Docker took the following steps:
# 1. The Docker client contacted the Docker daemon.
# 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
#    (amd64)
# 3. The Docker daemon created a new container from that image which runs the
#    executable that produces the output you are currently reading.
# 4. The Docker daemon streamed that output to the Docker client, which sent it
#    to your terminal.

# To try something more ambitious, you can run an Ubuntu container with:
# $ docker run -it ubuntu bash

# Share images, automate workflows, and more with a free Docker ID:
# https://hub.docker.com/

# For more examples and ideas, visit:
# $https://docs.docker.com/get-started/
```
OPTIONAL

Change the docker user if you do log out and then log back in again. This allows: you to use docker with out sudo.
```bash
sudo usermod -aG docker $USER
```

Upgrade Docker Engine

To upgrade Docker Engine, follow step 2 of the installation instructions, choosing the new version you want to install.