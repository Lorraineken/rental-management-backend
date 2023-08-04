from django.urls import path, include
#from rest_framework.routers import DefaultRouter
#from . import views
from .views import UnitCreate,UnitList,UnitDetail,UnitUpdate,UnitDelete

#router = DefaultRouter()
#router.register(r'units',views.UnitView)

#urlpatterns = [
#    path('', include(router.urls)),
#]

urlpatterns = [
    path('create/',UnitCreate.as_view(), name ='create-unit'),
    path('',UnitList.as_view()),
    path('<int:pk>/',UnitDetail.as_view(), name ='retrieve-unit'),
    path('update/<int:pk>', UnitUpdate.as_view(),name='update-unit'),
    path('delete/<int:pk>', UnitDelete.as_view(), name='delete-unit')
]



