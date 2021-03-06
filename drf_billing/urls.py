from django.urls import path
from . import views


app_name = 'drf_billing'

urlpatterns = [
    # ex: api/billing/list/
    path('list/', views.ShowBillView.as_view(), name='Show-Bill-Item'),
    # ex: api/billing/add/
    path('add/', views.AddBillingHeaderView.as_view(), name='Add-Bill-Item'),
    # ex: api/billing/show/bill/pk/
    path('show/bill/<int:pk>/', views.GetBillView.as_view(), name='Get Bill View'),
]
