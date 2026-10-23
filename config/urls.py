from django.contrib import admin
from django.urls import path
from gym import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="home"),
    path("turmas/", views.classesList, name="classesList"),
]
