# this file created by user
from django.urls import path, include
from . import views

app_name = "tthian"


urlpatterns = [
    path('', views.home, name='A_ttHomePathNameIn_AppUrls'),
    path('tt/', views.tt_home, name="A_tt_home"),
]
