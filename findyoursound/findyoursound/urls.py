"""
URL configuration for findyoursound project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from music.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/genres/", GenreView.as_view(), name="genres"),
    path("api/<str:genre_name>/artists/", GenreArtistView.as_view(), name="artists"),
    path("api/<str:genre_name>/gear/", ArtistGearView.as_view(), name="gear")
]
