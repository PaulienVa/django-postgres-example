# Usefull commands

Goal of this project is to have a simple set-up of an application connecting to a Postgres database.
This set-up was used to understand the same concepts as that were used on a Java application connecting to a database.

Those concepts were:
- Connecting to the database (configuration)
- Entity classes (or here Models)
- Query language

Name of the application `teachersapplication`.

## Run application

```commandline
python manage.py runserver
```

## Run database migrations

```commandline
python manage.py makemigrations
```

```commandline
python manage.py migrate
```

## Extra information


### Set-up
- This project was initialized using [PyCharm](https://www.jetbrains.com/pycharm/).
- The postgres integration was performed based on this [article](https://stackpython.medium.com/how-to-start-django-project-with-a-database-postgresql-aaa1d74659d8)
- Documentation about querying using Django can be found [here](https://docs.djangoproject.com/en/dev/topics/db/sql/)

## Application architecture
This is a REST api serving teachers and students saved in a postgres database.

Dependencies can be found in the [requirements.txt](requirements.txt). (If pip is complaining about pg_config: run `brew install postgresql` (on a mac)).

To access the application's endpoint, go to the [Django UI](http://localhost:8000/teachers/)


Configuration of the project can be found in [settings.py](djangoProject/settings.py).

Data model can be found in [application's models.py](teachersapplication/models.py).

## Install in local environment
1. Make sure postgres is running somewhere (change settings.py accordingly)
2. Create virtual environment using for instance [virtualenvwrapper](https://www.geeksforgeeks.org/using-mkvirtualenv-to-create-new-virtual-environment-python/)
3. Install the dependencies: `pip install requirements.txt`
4. Generate migrations: `python manage.py makemigrations`
5. Migrate the migrations `python manage.py migrate`
6. Run the server `python manage.py runserver`
7. In your browser go to [UI](http://localhost:8000/teachers/)
