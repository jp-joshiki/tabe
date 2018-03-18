tabe (食べ) means `eat` in Japanese

Access from [https://tabe.herokuapp.com](https://tabe.herokuapp.com)

# Dev env

Requirents: Docker, Python3.6, Pipenv

create `local_settings.py`, paste in

```python
DEBUG = True

SQLALCHEMY_DATABASE_URI = 'postgresql://user:passwd@localhost:5432/tabe'
```


```shell
$ docker-compose up
$ pipenv install
$ pipenv shell
$ python manage.py db upgrade
$ python manage.py update_tags
```

# Run spiders

```shell
python -m spiders
```
