from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('listings/', views.listing_list, name='listing_list'),
    path('listing/<int:pk>/', views.listing_detail, name='listing_detail'),
    path('listing/<int:pk>/available/', views.listing_available, name='listing_available'),
    path('listings/create/', views.ListingCreateView.as_view(), name='listing_create'),
    path('listing/<int:pk>/edit/', views.ListingUpdateView.as_view(), name='listing_update'),
    path('listing/<int:pk>/delete/', views.ListingDeleteView.as_view(), name='listing_delete'),
]
