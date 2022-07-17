from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('menu/', views.MenuView.as_view(), name='menu'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('booking/create/', views.Booking.as_view(), name='create'),
]
