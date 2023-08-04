from django.urls import path, include
from rest_framework.routers import DefaultRouter
#from . import views


from .views import TenantCreate,TenantList,TenantDetail,TenantUpdate,TenantDelete

#router = DefaultRouter()
#router.register(r'tenants',views.TenantView)

#urlpatterns = [
#    path('', include(router.urls)),
#]

urlpatterns = [
    path('create/',TenantCreate.as_view(), name ='create-tenant'),
    path('',TenantList.as_view()),
    path('<int:pk>/',TenantDetail.as_view(), name ='retrieve-tenant'),
    path('update/<int:pk>', TenantUpdate.as_view(),name='update-tenant'),
    path('delete/<int:pk>', TenantDelete.as_view(), name='delete-tenant')
]

