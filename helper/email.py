from rest_framework.authtoken.models import Token
from django.core.mail import send_mail
from django.conf import settings


def send_activation_email(user):

    # genrate new token
    token, created = Token.objects.get_or_create(user=user)

    # Create the activation URL using the auth_token and BASE_URL from settings
    activate_url = f"{ settings.BASE_URL }/account_activation/{ token.key }"

    # Create the email subject and message
    subject = 'Activate your account'
    message = f'Click the link below to activate your account:\n\n{activate_url}'

    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])


# def send_order_email(owner_email, product_obj, customer_obj):
#     subject = "New Order Arriving"
#     data = {
#         "customer_email":customer_obj.user,
#         "customer_phone": customer_obj.phone,
#         "customer_address": customer_obj.address,
#         "car": product_obj.company_name +" "+ product_obj.model_name,
#         "car_number":product_obj.car_number,
#     }
#     message = get_template("order_car.html").render(data)
#     mail = EmailMessage(
#         subject=subject,
#         body=message,
#         from_email=settings.EMAIL_HOST_USER,
#         to=[owner_email],
#         reply_to=[settings.EMAIL_HOST_USER],
#     )
#     mail.content_subtype = "html"
#     mail.send()
#     return True
