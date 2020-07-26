from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.welcome, name="welcome"),
    path('scrapy', views.Scrapy, name="scrapy"),
    path('dataScraping', views.dataScraping, name="dataScraping"),
]
