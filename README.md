# Link Scraping

Link Scraping is a web application developed in Python where users can provide an URL and the application will find all the links inside this URL and then, all links inside the newly found links.

## Usage

-  Clone the project
```
git clone https://github.com/IgorGMoraes/Link-Scraping.git
```
<br>

### Run locally
-  With Python installed, install pipenv
```
pip install pipenv
```
<br>

-  Download geckodriver and paste it into the python root folder
https://github.com/mozilla/geckodriver/releases <br>
*This step is not necessary if you run in docker*
<br>

-  Install depencencies
```
pipenv install --system --deploy
```
<br>

-  Then run the application
```
python link_scraping/manage.py runserver
```
<br>

### Run in docker
-  With Docker installed, create the containers and run the application with
```
docker-compose up
```
- If the continer was already created, just run it 
```
docker-compose start
```
<br>

- To stop the contain
```
docker-compose stop
```
- To stop and also remove all networks and volumes
```
docker-compose down
```

### Access the application
```
http://localhost:8000
```
