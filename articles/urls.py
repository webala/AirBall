from django.urls import path
from .views import article_create_view, article_list_view

urlpatterns = [
    path('create', article_create_view),
    path('article_list', article_list_view, name='article_list')
]