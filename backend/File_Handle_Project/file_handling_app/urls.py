# urls.py
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import FileView,UserRegistrationView

urlpatterns = [
    path('documents/<str:filename>', FileView.as_view(), name='file-handler'),
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
