from django.urls import path
from . import views

app_name='securef'
urlpatterns=[
    path("", views.intro, name="intro"),
    path("admlogin", views.adm,name="adm"),
    path("emplogin", views.emp,name="emp"),
    path("addloc",views.adm_job,name="secure"),
    path("admentry",views.adm_entry,name="admentry"),
    ]