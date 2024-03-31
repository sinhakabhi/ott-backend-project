# ott_app/viewership/urls.py
from django.urls import path
from .views import HomeView, WatchVideoView, RegisterView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('home/', HomeView.as_view(), name='last_viewed_videos'),
    path('watch-video/', WatchVideoView.as_view(), name='log_viewed_video'),
    path('register/', RegisterView.as_view(), name='create_customer'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
