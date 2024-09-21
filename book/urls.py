

from django.urls import path
from book import views
from .views import success, show_book_content





urlpatterns = [
    path('add_books/', views.create_book),
    path('success', views.success, name='book_added'),

   
    
    ]