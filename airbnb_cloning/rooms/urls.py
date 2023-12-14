from django.urls import path
from . import views

app_name = 'rooms'
urlpatterns = [
    path('', views.index),
    path('<int:room_id>/', views.detail),
    path('reviews/', views.reviews),
    path('<int:room_id>/book/', views.book),
    # path('create/', views.create),
    # path('<int:pk>/delete/', views.delete),
    # path('<int:pk>/update/', views.update),
]
