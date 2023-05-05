from django.urls import path

from authentication.views import CreateUserView, UserLoginView, SendActivationEmailView, ActivateAccountView


urlpatterns = [
    path('users/', CreateUserView.as_view(), name="create_user"),
    path('login/', UserLoginView.as_view(), name="user_login"),
    path('send_activation_link/', SendActivationEmailView.as_view(), name="send_activation_link"),
    path('activate_account/<str:token>', ActivateAccountView.as_view(), name="activate_account")
]
