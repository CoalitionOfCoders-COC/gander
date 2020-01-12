from django.urls import path
from . import views

'''
    this is the routing for the webapp will be linked to main urls.py from the parent dir 'project'
'''
app_name = 'webapp'
urlpatterns = [
    path('', views.landing, name="landing"),
    path('index/', views.index, name="index")

]