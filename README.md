# Apache
Parse Apache log files

## Installation

1) `git clone https://github.com/ArtyomViryutin/Apache.git`


2) In the project folder create .env.dev file and set up following variables:

`SECRET_KEY=<Your SECRET_KEY>`

`DEBUG=<0 or 1>`

`ALLOWED_HOSTS=<e.g. localhost 127.0.0.1>`

`DATABASE_ENGINE=django.db.backends.postgresql`

`DATABASE_NAME=postgres`

`DATABASE_USER=postgres`

`DATABASE_PASSWORD=postgres`

`DATABASE_HOST=db`

`DATABASE_PORT=5432`

3) `$ docker-compose up --build`

## Usage
### Parse Apache log file
`$ docker-compose exec web python manage.py parse <url_1 url_2 url_3...>`

### Get results

1) `$ docker-compose exec web python manage.py createsuperuser`
   

2) http://localhost:8000/admin/