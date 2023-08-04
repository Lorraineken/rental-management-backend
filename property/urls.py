from django.urls import path, include
from rest_framework.routers import DefaultRouter
#from . import views
from .views import PropertyCreate,PropertyList,PropertyDetail,PropertyUpdate,PropertyDelete

#router = DefaultRouter()
#router.register(r'propertys',views.PropertyView)

#urlpatterns = [
#    path('', include(router.urls)),
#]

urlpatterns = [
    path('create/',PropertyCreate.as_view(), name ='create-property'),
    path('',PropertyList.as_view()),
    path('<int:pk>/',PropertyDetail.as_view(), name ='retrieve-property'),
    path('update/<int:pk>', PropertyUpdate.as_view(),name='update-property'),
    path('delete/<int:pk>', PropertyDelete.as_view(), name='delete-property')
]
