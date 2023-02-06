from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('beyonces/', views.beyonces_index, name='index'),
    path('beyonces/<int:beyonce_id>/', views.beyonces_detail, name='detail'),
    path('beyonces/create/', views.BeyonceCreate.as_view(), name='beyonces_create'),
    path('beyonces/<int:pk>/update/', views.BeyonceUpdate.as_view(), name='beyonces_update'),
    path('beyonces/<int:pk>/delete/', views.BeyonceDelete.as_view(), name='beyonces_delete'),
    path('beyonces/<int:beyonce_id>/add_shows/', views.add_shows, name='add_shows'),
    path('beyonces/<int:beyonce_id>/add_photo/', views.add_photo, name='add_photo'),
    path('beyonces/<int:beyonce_id>/assoc_tours/<int:tour_id>/', views.assoc_tours, name='assoc_tours'),
    path('tours/create/', views.TourCreate.as_view(), name='tours_create'),
    path('tours/', views.TourIndex.as_view(), name='tours_index'),
    path('tours/<int:pk>/', views.ToursDetail.as_view(), name='tours_detail'),
    path('tours/<int:pk>/update/', views.TourUpdate.as_view(), name='tours_update'),
    path('tours/<int:pk>/delete/', views.TourDelete.as_view(), name='tours_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]