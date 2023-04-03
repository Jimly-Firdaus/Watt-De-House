# Watt-De-House

# Runner Setup
## How to Activate Runner from Scratch
* Go to root of this project
* Ensure that you have Docker Desktop installed and opened
* Open terminal then 
```bash
docker build -t <image-name> .
```
* Specify the <image-name>
* Then run image with
```bash
docker run -d --name <runner-name> -v /var/run/docker.sock:/var/run/docker.sock <image-name>:latest
```

## How to Activate Runner from Docker Registry
* Ensure that you have Docker Desktop installed and opened
* Open terminal then
```bash
docker pull jimlyfirdaus/gitlab-runner-5
```
* Then run image with
```bash
docker run -d --name <runner-name> -v /var/run/docker.sock:/var/run/docker.sock <image-name>:latest
```

## Reference
* https://docs.gitlab.com/runner/install/docker.html
* https://docs.gitlab.com/runner/register/index.html#docker

# How to Enable Auto Lint Python Files
1. Make sure you have already installed `black`
```bash
pip install black
``` 
2. Then go to root of this project:
```bash
.\black.setup.bat
```
3. Black should be triggered after this when staging files
