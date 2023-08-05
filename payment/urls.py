from django.urls import path
from .views import PaymentCreateView, PaymentListView, PaymentDetailView, PaymentUpdateView, PaymentDeleteView

urlpatterns = [
    path('create/', PaymentCreateView.as_view(), name='create-payment'),
    path('list/', PaymentListView.as_view(), name='list-payments'),
    path('<int:pk>/', PaymentDetailView.as_view(), name='retrieve-payment'),
    path('update/<int:pk>/', PaymentUpdateView.as_view(), name='update-payment'),
    path('delete/<int:pk>/', PaymentDeleteView.as_view(), name='delete-payment'),
]
