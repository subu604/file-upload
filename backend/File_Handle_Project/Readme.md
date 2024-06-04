# Django "File Handle Project" App

As an example of how to build a new Django app

Corresponding blog posts:

* [Building a Django App and Deploying It on Heroku](https://stefanbschneider.github.io/blog/django-heroku). Corresponds to [release v1.0](https://github.com/stefanbschneider/django-hello-world/releases/tag/v1.0.0).
* [Adding Google Analytics to a Django App](https://stefanbschneider.github.io/blog/django-google-analytics). Corresponds to [release v1.1](https://github.com/stefanbschneider/django-hello-world/releases/tag/v1.1.0).
* [Adding a Database to a Django App](https://stefanbschneider.github.io/blog/django-db). Corresponds to [release v1.2](https://github.com/stefanbschneider/django-hello-world/releases/tag/v1.2.0).
* [Using Bootstrap to Style a Django App](https://stefanbschneider.github.io/blog/django-bootstrap). Corresponds to [release v1.3](https://github.com/stefanbschneider/django-hello-world/releases/tag/v1.3.0).

## Setup

```
pip install -r requirements
python manage.py make migrations
python manage.py migrate
```

## Usage
```
* Initially User Registers with a username and password
* Generates the token using the registered username and password
* Using the token uploads a file to dbsqlite3 database
* If same filename is uploaded then there will be version number comes up.
* user can try to fetch the uploaded pdfs with details 
```

### Development

```
python manage.py runserver
```

The app is running on http://localhost:8000/

** Attached a postman collection to run the application and give a try in local using postman 

