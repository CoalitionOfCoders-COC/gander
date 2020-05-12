[![Gitpod Ready-to-Code](https://img.shields.io/badge/Gitpod-Ready--to--Code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/eesayas/Gander) 

# Gander
Gander is a web app for deciding what movies to watch with only a limited time

### Accessing admin dashboard
1. Go to '/admin' route
2. Enter the following credentials...
```
Username: johndoe
Password: password
```

[Netfix Data: netflix_titles.csv](https://github.com/eesayas/Gander/blob/master/netflix_titles.csv)

### Entering data from netflix_titles.csv

1. Make a model in './webapp/models.py'

```
# This is a Movie object that will be stored in the DB
class Movie(models.Model):
    movie_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    duration = models.IntegerField()

    def __str__(self):
        return self.name
```

2. Add config to './webapp/apps.py'

```
class WebappConfig(AppConfig):
    name = 'webapp'
```

3. Add config to './project/settings.py'

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'webapp.apps.WebappConfig'          #added config
]
```

4. Go to './webapp/admin.py' to register model

```
from django.contrib import admin
from .models import Movie

# Register your models here.
admin.site.register(Movie)
```

5. Make migrations

```
python3 manage.py makemigrations
python3 manage.py migrate
```

6. Enter python shell

```
python3 manage.py shell
```

7. ***in Python Shell*** enter the following...

```
>>> from webapp.models import Movie
>>> import csv

>>> with open('netflix_titles.csv') as csvfile: 
...:     reader = csv.DictReader(csvfile) 
...:     for row in reader: 
...:         if row['type'] == 'Movie': 
...:             p = Movie(movie_id=row['show_id'],name=row['title'],duration=int(row['duration'].split()[0])) 
...:             p.save() 
...: 
>>> exit()
```

`NOTE`: You have to wait until `...` does not show up anymore before you `exit()`.
Because it will take time to load/read the data into the DB.
Another indicator might be a '.journal' file in the root dir. 
When '.journal' is present and changing, loading/reading is happening.
After '.journal' becomes missing and no longer present, the loading/reading is done.

8. Runserver again

```
python3 manage.py runserver
```

9. Check '/admin' if imported .csv data is present