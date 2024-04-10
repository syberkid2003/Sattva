"""
URL configuration for quiz project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from webapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("" , login , name="login"),
    path("signup/",signup , name="signup"),
    path("home/" ,home , name="home"),
    path("test/<int:val>" ,test , name="test"),
    path("setting/update-profile/" ,update , name="update"),
    path("setting/view-profile" ,profile , name="profile"),
    path("setting/logout-profile" ,logout , name="logout"),
    path("settings/forgot-passkey/" , forgot , name="forgot" ),
    path("settings/login-unable/forgot-passkey/reset-password/<int:key>" , reset , name="reset" ),
    path("settings/forgot-passkey/updated", updatedpasskey , name="passkey_done"),
    path("test/ongoing" , setup , name ="setup")
]
