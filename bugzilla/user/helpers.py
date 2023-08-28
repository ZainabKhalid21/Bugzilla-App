from django.core.mail import send_mail
from django.conf import settings


def send_forgot_password_mail(email):

    subject = 'Your forget password link'
    message = f'hi , click on the link to reset your password http://localhost:8000/change_password/'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail (subject , message , email_from , recipient_list )
    return True

