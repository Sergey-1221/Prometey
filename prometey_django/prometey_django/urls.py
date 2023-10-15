"""prometey_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from map.views import *
from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    path("", ind),
    path("admin/", admin.site.urls),
    path("get_arrow/<int:path>", getjson_arrow),
    path("kamen/", index, name='index'),
    path("zavod/", zavod, name='zavod'),
    path("alitic/", alitic, name='alitic'),
    path("login/", register_view, name='login'),
    path("department/", department, name='department'),
    path("oborudovanie/", oborudovanie, name='oborudovanie'),
    path("sensors/", sensors, name='sensors'),
    path("employs/", employs, name='employs'),
    path("employs/<int:pk>", employ_view, name='employ_view'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
