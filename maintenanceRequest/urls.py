from django.urls import path
from .views import (
    MaintenanceRequestCreate,
    MaintenanceRequestList,
    MaintenanceRequestDetail,
    MaintenanceRequestUpdate,
    MaintenanceRequestDelete,
)

urlpatterns = [
    path('create/', MaintenanceRequestCreate.as_view(), name='create-maintenance-request'),
    path('', MaintenanceRequestList.as_view(), name='maintenance-request-list'),
    path('<int:pk>/', MaintenanceRequestDetail.as_view(), name='maintenance-request-detail'),
    path('update/<int:pk>/', MaintenanceRequestUpdate.as_view(), name='update-maintenance-request'),
    path('delete/<int:pk>/', MaintenanceRequestDelete.as_view(), name='delete-maintenance-request'),
]
