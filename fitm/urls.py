"""fitm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from monitoring import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('test/', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('monitor/', views.monitor, name='monitor'),
    path('topology/', views.topology, name='page3'),
    path('infodevice/', views.infodevice, name='page4'),
    path('report/', views.report, name='report'),
    path('register/', views.register, name='register'),
    path('registeradmin/', views.registeradmin, name='registeradmin'),
    path('addUser', views.addUser),
    path('wlc', views.wlc_ap),
    path('topology_serach', views.topology_serach),
    path('login', views.login, name='login'),
    path('main1', views.main1, name='main1'),
    path('logout/', views.logout, name='logout')
] 
