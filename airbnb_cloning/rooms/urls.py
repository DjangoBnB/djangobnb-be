from django.urls import path
from . import views

app_name = 'rooms'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:room_id>/', views.detail, name='detail'),
    path('reviews/', views.reviews, name='reviews'),
    path('<int:room_id>/book/', views.book, name='book'),
    # path('create/', views.create, name='create'),
    # path('<int:pk>/delete/', views.delete, name='delete'),
    # path('<int:pk>/update/', views.update, name='update'),
]
