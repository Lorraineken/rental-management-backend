from django.urls import path
from .views import AgreementListView, AgreementDetailView, AgreementCreateView, AgreementUpdateView, AgreementDeleteView

urlpatterns = [
    path('agreements/', AgreementListView.as_view(), name='agreement-list'),
    path('agreements/create/', AgreementCreateView.as_view(), name='agreement-create'),
    path('agreements/<int:pk>/', AgreementDetailView.as_view(), name='agreement-detail'),
    path('agreements/<int:pk>/update/', AgreementUpdateView.as_view(), name='agreement-update'),
    path('agreements/<int:pk>/delete/', AgreementDeleteView.as_view(), name='agreement-delete'),
]

