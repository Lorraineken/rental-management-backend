from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


from .views import TenantList

#router = DefaultRouter()
#router.register(r'tenants',views.TenantView)

#urlpatterns = [
#    path('', include(router.urls)),
#]

urlpatterns = [
    path('',TenantList.as_view()),
]

