from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.core.mail import send_mail
# from django.conf import settings
# from django.urls import reverse
# from django.utils.crypto import get_random_string


# class User(AbstractUser):
#     auth_token = models.CharField(max_length=255, blank=True)

#     def send_activation_email(self):
#         # Generate a random auth_token and save it to the user's model
#         self.auth_token = get_random_string(64)
#         self.save()
#         # Create the activation URL using the auth_token and BASE_URL from settings
#         activate_url = reverse('account_activation', args=[self.auth_token])
#         activate_url = settings.BASE_URL + activate_url
#         # Create the email subject and message
#         subject = 'Activate your account'
#         message = f'Click the link below to activate your account:\n\n{activate_url}'
#         # Send the email using the send_mail function
#         send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [self.email])
