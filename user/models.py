from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# Create your models here.

class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email field required')
        
        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('name', 'Admin')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('SuperUser must have is_staff= True')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('SuperUser must have is_seperuser= True')

        return self._create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique = True)
    name = models.CharField(max_length =100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.email}"


class AdminUpload(models.Model):
    user = models.ForeignKey('CustomUser', related_name='admin_upload', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    Image =models.ImageField()
    Date = models.DateField()

    def __str__(self):
        return self.user.email
    
