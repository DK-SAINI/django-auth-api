from django.urls import path

from authentication.views import CreateUserView


urlpatterns = [
    path('users/', CreateUserView.as_view(), name="create_user"),
]
