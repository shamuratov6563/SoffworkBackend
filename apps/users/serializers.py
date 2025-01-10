from rest_framework.exceptions import ValidationError
from django.core.cache import cache
from rest_framework import serializers
import re
from .models import User
from .utils import send_confirmation_code_to_user, generate_confirmation_code, send_verification_code_to_user

def isphone(phone):
    phone_regex = r"^\+998\d{9}$" 
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
            username = phone_or_email  
            user, created = User.objects.get_or_create(phone_number=phone_or_email)
        elif auth_type == 'email': 
            username = phone_or_email
            user, created = User.objects.get_or_create(email=phone_or_email)

            if not created and user.auth_status == 'confirmed':
                raise ValidationError(
                "Foydalanuvchi allaqachon mavjud. Iltimos, boshqa telefon raqami yoki email kiriting.")
        user.username = username  
        user.set_password(password)
        user.save()
        confirmation_code = generate_confirmation_code()
        cache.set(f"confirmation_code_{user.id}", confirmation_code, timeout=300)
        if auth_type == 'email':
            send_confirmation_code_to_user(user, confirmation_code)  
        elif auth_type == 'phone_number':
            send_verification_code_to_user(user, confirmation_code)

        return user
    
    def to_representation(self, instance):
        return {
            'user_id': instance.id
        }

class ConfirmationCodeSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    code = serializers.CharField()



