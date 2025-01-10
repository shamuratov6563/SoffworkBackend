from django.core.cache import cache
from django.core.mail import send_mail
from django.conf import settings
import random
import string


def generate_confirmation_code():
    return ''.join(random.choices(string.digits, k=6))

def send_confirmation_code_to_user(user, code):

    subject = 'Tasdiqlash Kodingiz'
    message = f'Sizning tasdiqlash kodingiz: {code}'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [user.email]
    try:
        send_mail(subject, message, from_email, recipient_list)
    except Exception as e:
        print(f"Error while sending email: {str(e)}")


def send_verification_code_to_user(user, code):
    print(f"Verification code: {str(code)}")
    