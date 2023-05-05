from django.urls import path

from authentication.views import CreateUserView, UserLoginView


urlpatterns = [
    path('users/', CreateUserView.as_view(), name="create_user"),
    path('login/', UserLoginView.as_view(), name="user_login"),
]
