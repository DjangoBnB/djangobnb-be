from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('signup/', include('dj_rest_auth.registration.urls')),
    path('update/', views.update),
    path('likes/', views.likes),
    # path('dj-rest-auth/facebook/', views.FacebookLogin.as_view()),
    # path('dj-rest-auth/google/', views.GoogleLogin.as_view())
    path('', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)