"""eightproject URL Configuration

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
from bankapp import views as v1
from countryapp import views as v2
from courseapp import views as v3

urlpatterns = [
    path('admin/', admin.site.urls),
    path('deposit/',v1.deposit),
    path('withdraw/',v1.withdraw),
    path('balance/',v1.balance),
    path('India/',v2.India),
    path('USA/',v2.USA),
    path('uc1/',v3.uc1),
    path('uc2/',v3.uc2),
    path('uc3/',v3.uc3),
    
    
]
