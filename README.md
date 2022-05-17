# APM Elastic
Elastic APM


## install Docker 

```
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```

```
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

```

## Dependência lib psycopg
```
sudo apt install postgresql nginx
sudo apt-get install libpq-dev python-dev
service postgresql stop
```
## Instalando o projeto  

```
cd apm_lab
apt install python3-pip
git clone https://github.com/diogolimaelven/apm_elastic.git
pip3 install --no-cache-dir -r requirements.txt
cp default /etc/nginx/sites-enabled/default

python3 apm.py &

```
