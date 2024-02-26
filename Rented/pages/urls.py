from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('listings/', views.listing_list, name='listing_list'),
    path('listing/<int:pk>/', views.listing_detail, name='listing_detail'),
]