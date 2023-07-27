"""
URL configuration for rentalBackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
##Added import
from rest_framework import routers
from agreement import views

##Setting up router(api)
router = routers.DefaultRouter()
router.register(r'agreements',views.AgreementView, 'agreement')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agreement/',include(router.urls)),
]
