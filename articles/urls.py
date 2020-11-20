from django.urls import path
from .views import article_create_view 

urlpatterns = [
    path('create', article_create_view)
]