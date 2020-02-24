from django.urls import path
from . import views

urlpatterns = [
    path('', views.total_years, name='total_years'),
    path('revenuerank/', views.revenue_rank, name='revenue_rank'),
    path('import/', views.importfilmes, name='importfilmes')
]
