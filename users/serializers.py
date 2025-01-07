from rest_framework import serializers
import re
from .models import User
from rest_framework.response import Response
from rest_framework import status

def isphone(phone):
    phone_regex = r"^\+998\d{9}$"  # +998 bilan boshlanadigan va 9 raqamdan iborat telefon raqami
    return re.match(phone_regex, phone) is not None

def isemail(email):
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$" 
    return re.match(email_regex, email) is not None

class UserSerializer(serializers.Serializer):
    phone_or_email = serializers.CharField() 
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        phone_or_email = attrs.get('phone_or_email')
        if isphone(phone_or_email):
            auth_type = 'phone_number'
        elif isemail(phone_or_email):
            auth_type = 'email'
        else:
            raise serializers.ValidationError("Iltimos, telefon raqam yoki email kiritishingiz kerak.")
        attrs['auth_type'] = auth_type
        return super().validate(attrs)

    
    def create(self, validated_data):
        phone_or_email = validated_data.get('phone_or_email')
        password = validated_data.get('password')
        auth_type = validated_data.get('auth_type')

        if auth_type == 'phone_number':  
            username = f"{phone_or_email}"  
            user, created = User.objects.get_or_create(phone_number=phone_or_email)
        elif auth_type == 'email': 
            username = f"{phone_or_email}" 
            user, created = User.objects.get_or_create(email=phone_or_email)

        if created:
            original_username = username
            counter = 1
            while User.objects.filter(username=username).exists():
                username = f"{original_username}_{counter}"
                counter += 1
            
            user.username = username  
            user.set_password(password)
            user.save()

            send_confirmation_code_to_user(user)

        return user
    

    def to_representation(self, instance):
        return {
            'user_id': instance.id
        }


from django.core.cache import cache
import random
import string
from datetime import timedelta

def generate_confirmation_code():
    return ''.join(random.choices(string.digits, k=6))

def send_confirmation_code_to_user(user):
    confirmation_code = generate_confirmation_code()
    
    cache.set(f"confirmation_code_{user.email}", confirmation_code, timeout=120)

    