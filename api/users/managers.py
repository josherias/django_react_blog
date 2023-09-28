from django.contrib.auth.base_user import BaseUserManager

""" 
    Manager is a class that provides an interface through which database query operations 
    are provided to Django models
"""


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('User must have an email address!')
        if not password:
            raise ValueError('User must have a password!')
        email= self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Super user must be staff')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Super user must be true')
        
        return self.create_user(email, password, **extra_fields)