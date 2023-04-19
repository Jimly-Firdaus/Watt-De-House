# Watt-De-House

# General Information
Program ini dibuat untuk menyelesaikan Tugas Implementasi IF2250 Rekayasa Perangkat Lunak. Program ini memiliki dua fitur utama yaitu Estimator dan Simulator. Fitur Estimator berfungsi untuk mengkalkulasi perkiraan biaya yang harus dikeluarkan untuk konsumsi listrik. Fitur ini meminta input data perangkat listrik serta estimasi durasi penggunaan dari perangkat listrik tersebut. Fitur Simulator berfungsi untuk melakukan simulasi perangkat listrik yang ada di rumah. Fitru ini meminta input data perangkat listrik, circuit breaker, dan ruangan. Setelah itu, program aka mensimulasikan apakah terjadi electrical overload atau tidak jika perangkat listrik dinyalakan secara bersamaan. 

# How To Run Program
1. Clone repository
```
git clone "https://gitlab.informatika.org/Jimly-Firdaus/watt-de-house.git"
```
2. Masuk ke directory tempat repository disimpan

3. Masuk ke folder src
```
cd src
```
4. Jalankan Program
```
python main.py
```


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
docker run -d --name <runner-name> -v /var/run/docker.sock:/var/run/docker.sock <image-name>:<version>
```

## How to Activate Runner from Docker Registry
* Ensure that you have Docker Desktop installed and opened
* Open terminal then
```bash
docker pull jimlyfirdaus/gitlab-runner-concurrent
```
* Then run image with
```bash
docker run -d --name <runner-name> -v /var/run/docker.sock:/var/run/docker.sock <image-name>:<version>
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
