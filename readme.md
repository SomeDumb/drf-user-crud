# Simple crud for users

## Deploy

deployed on heroku using [Dockerfile](https://github.com/SomeDumb/emphasoft/blob/main/Dockerfile) and [heroku.yml](https://github.com/SomeDumb/emphasoft/blob/main/heroku.yml)

**[LINK](https://infinite-dawn-85986.herokuapp.com)**

> username: user  
> password: password

## Dev

For dev purposes used [docker-compose.yml](docker-compose.yml)

To run simply create .env.  

.env example:
```sh
SECRET_KEY='SomeSecretKey'
DEBUG=True
SQL_ENGINE='django.db.backends.postgresql'
SQL_DATABASE='emphasoft_db'
SQL_USER='user'
SQL_PASSWORD='password'
SQL_HOST='db'
SQL_PORT=5432
```

Then run
```sh
docker-compose up
```

### Fixes

Validation fixed by adding update and create methods to [serializer](https://github.com/SomeDumb/emphasoft/blob/main/api/serializers.py).
