from django.urls import path
from .views import CustomerView


urlpatterns = [
    path('contact/', CustomerView.as_view(), name='contact'),
]
