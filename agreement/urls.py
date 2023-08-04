from django.urls import path, include
#from rest_framework.routers import DefaultRouter
#from . import views
from .views import AgreementCreate,AgreementList,AgreementDetail,AgreementUpdate,AgreementDelete

#router = DefaultRouter()
#router.register(r'agreements',views.AgreementView)

#urlpatterns = [
#    path('', include(router.urls)),
#]

urlpatterns = [
    path('create/',AgreementCreate.as_view(), name ='create-agreement'),
    path('',AgreementList.as_view()),
    path('<int:pk>/',AgreementDetail.as_view(), name ='retrieve-agreement'),
    path('update/<int:pk>', AgreementUpdate.as_view(),name='update-agreement'),
    path('delete/<int:pk>', AgreementDelete.as_view(), name='delete-agreement')
]
