[![Gitpod Ready-to-Code](https://img.shields.io/badge/Gitpod-Ready--to--Code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/eesayas/Gander) 

# Gander
Gander is a web app for deciding what movies to watch with only a limited time

### ***Gander* won second place in CMPUT401 Winter 2020 Hackathon!**
Read more in this [article](https://www.cybera.ca/news-and-events/tech-radar/university-hackathon-shows-students-the-wide-possibilities-of-cloud/) by Cybera

### Accessing admin dashboard
1. Go to '/admin' route
2. Enter the following credentials...
```
Username: johndoe
Password: password
```
OR

### Create a superuser
```
python3 manage.py createsuperuser
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
    cover_photo = models.CharField(max_length=10000, default='https://www.voiceofsandiego.org/wp-content/uploads/2013/08/film081513.jpg')

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

### Webscraping netflix page for movie pictures

**NOTE:** You may need to install some packages before starting console/shell

```
pip3 install requests
pip3 install lxml
```

In python console/shell:
```
from webapp.models import Movie
import requests
from lxml import html

data = Movie.objects.all()
for m in data:
    try:
        page_url = 'https://www.netflix.com/title/' + m.movie_id
        page = requests.get(page_url)
        tree = html.fromstring(page.content)
        image = tree.xpath("//*[contains(@class, 'hero-image-mobile')]/@style")
        photo_url = image[0].split('"')[1].split('"')[0]
        m.cover_photo=photo_url
        m.save()
        print(photo_url)
    except Exception as e:
        print(e)
        pass 
```