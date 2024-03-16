from django.urls import path
from .views import welcome, result, add_entry, data_mining, list_entries

urlpatterns = [
    path('welcome/', welcome, name='welcome'),
    path('result/', result, name='result'),
    path('add_entry/', add_entry, name='add_entry'),
    path('data_mining/', data_mining, name='data_mining'),
    path('list_entries/', list_entries, name='list_entries'),  # Added for listing entries within a range
]
