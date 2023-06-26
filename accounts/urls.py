from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout, name="logout"),
    path("about/", views.about, name="about"),
    path("bmi/", views.bmi, name="bmi"),
    path("track/", views.track, name="track"),
    path("diet/", views.diet, name="diet"),
    path("execersice/", views.execersice, name="execersice"),
    path("veg/", views.veg, name="veg"),
    path("non/", views.veg, name="non"),
    path("keto/", views.veg, name="keto"),
    path("lowcarb/", views.veg, name="lowcarb"),
    path("weightl/", views.veg, name="weightl"),
    path("weightgain/", views.veg, name="weightgain"),

]

