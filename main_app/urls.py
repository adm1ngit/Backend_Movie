from django.urls import path
from .views import *

urlpatterns = [
    path('api/films/', FilmListAPIView.as_view()),
    path('api/Category/', CategoryListAPIView.as_view()),
    path('api/register/', UserRegisterView.as_view()),
    path('api/login/', LoginView.as_view()),
    path('api/CustomUsers/', UserListAPIView.as_view()),
]
