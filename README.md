# Getting Start

## 1. Setting Up `.env` Files
- Go to directory `archaeologyMain`.
- Create `.env`
```sh
SECRET_KEY = "YourSpeacialKey"
```

## 2. Setting Up `virtualenv` Files
- Setup the virtualenv!
  - `pip install virtualenv`
- Go to directory `archaeologyMain`
  - `virtualenv animated-octo-winner`
  - `source bin/activate`

## 3. Setting up Docker & Migrations & Create Super User

- You must the be directory `archaeologyMain`

```sh
docker-compose build
```

- Migration from Docker

```sh
docker-compose run django-archaeology python manage.py migrate
```

- Create Super User

```sh
docker-compose run django-archaeology python manage.py createsuperuser
```

- Run the Docker

```sh
docker-compose up
```

- Now you can go to [127.0.0.1:8000](127.0.0.1:8000) to see it live. 🚀
- Admin panel [127.0.0.1:8000/admin](127.0.0.1:8000/admin)
- You can create what u want!