from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'about_page'
urlpatterns = [
    path('', views.index, name='about')
]