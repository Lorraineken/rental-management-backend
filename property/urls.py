from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'propertys',views.PropertyView)

urlpatterns = [
    path('', include(router.urls)),
]
