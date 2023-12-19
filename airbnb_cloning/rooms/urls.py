from django.urls import path
from . import views

app_name = 'rooms'
urlpatterns = [
    path('', views.index),
    path('<int:room_id>/', views.detail),
    path('<int:room_id>/likes/', views.likes),
    path('reviews/', views.reviews),
    path('<int:user_id>/book_list/', views.book_list),
    path('book/<int:book_id>/', views.book_detail),
    # path('create/', views.create),
    # path('<int:pk>/delete/', views.delete),
    # path('<int:pk>/update/', views.update),
]
