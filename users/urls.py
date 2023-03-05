from django.urls import path
from .apiviews import RegisterApi#, LoginApi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView, TokenBlacklistView

urlpatterns = [
    #path('login/', LoginApi.as_view()),
    path('register/', RegisterApi.as_view()),
    path('token/',  TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/',  TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
]