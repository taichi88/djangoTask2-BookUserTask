
from django.urls import path

from reader import views as reader_view
from book import views as book_views






urlpatterns = [
    path('fillform/', reader_view.create_reader),
    path('book_info', book_views.show_book_content, name='book_info')
    
    ]