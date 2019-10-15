
from django.urls import path, include
from .views import Frontend

urlpatterns = [
    path('', Frontend.as_view())
]