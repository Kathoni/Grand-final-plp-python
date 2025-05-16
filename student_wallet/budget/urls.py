from django.urls import path
from . import views

app_name = 'budget'

urlpatterns = [
    path('', views.home, name='home'),
    path('add_category/', views.add_category, name='add_category'),
    path('add_transaction/', views.add_transaction, name='add_transaction'),
    path('edit_category/<int:category_id>/', views.edit_category, name='edit_category'),
    path('delete_category/<int:category_id>/', views.delete_category, name='delete_category'),
    path('edit_transaction/<int:transaction_id>/', views.edit_transaction, name='edit_transaction'),
    path('delete_transaction/<int:transaction_id>/', views.delete_transaction, name='delete_transaction'),
]