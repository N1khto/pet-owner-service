from django.urls import path

from pet_app.views import index


urlpatterns = [
    path("", index, name="index"),

]


app_name = "pet_app"
