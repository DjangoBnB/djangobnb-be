from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    # path('<int:room_pk>/', views.detail),    
    # path('create/', views.create),
    # path('<int:pk>/delete/', views.delete),
    # path('<int:pk>/update/', views.update),
]

