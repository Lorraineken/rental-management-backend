from django.urls import path, include
#from rest_framework.routers import DefaultRouter
#from . import views
from .views import LandlordCreate,LandlordList,LandlordDetail,LandlordUpdate,LandlordDelete

#router = DefaultRouter()
#router.register(r'landlords',views.LandlordView)

#urlpatterns = [
#    path('', include(router.urls)),
#]

urlpatterns = [
    path('create/',LandlordCreate.as_view(), name ='create-landlord'),
    path('',LandlordList.as_view()),
    path('<int:pk>/',LandlordDetail.as_view(), name ='retrieve-landlord'),
    path('update/<int:pk>', LandlordUpdate.as_view(),name='update-landlord'),
    path('delete/<int:pk>', LandlordDelete.as_view(), name='delete-landlord')
]


