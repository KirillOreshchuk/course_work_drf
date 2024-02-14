from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import (UserListView, UserDetailView, UserUpdateView,
                         UserDeleteView, UserCreateView, UserRegistrationView)

app_name = UsersConfig.name

urlpatterns = [
    path('', UserListView.as_view(), name='user_list'),
    path('create/', UserCreateView.as_view(), name='user_create'),
    path('<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),
    path('registration/', UserRegistrationView.as_view(), name='user_registration'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
