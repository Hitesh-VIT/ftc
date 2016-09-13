"""ftc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from ftc_back.views import Question_v,answer_v,profile_v
from django.conf.urls import include
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^question/',Question_v,name='question'),
    url(r'^answer/',answer_v),
    url(r'^profile/',profile_v),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework'))
]
