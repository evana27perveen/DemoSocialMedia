from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from App_login import views

app_name = 'App_login'

urlpatterns = [
    path('register/', views.registerAPIView),
    path('token/', TokenObtainPairView.as_view()),
    path('refresh-token/', TokenRefreshView.as_view()),
]
