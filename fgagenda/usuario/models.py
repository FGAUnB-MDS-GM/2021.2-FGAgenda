from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        user = self.model(email=self.normalize_email(email),
                          password=password,
                          is_active=True,
                          **extra_fields)

        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self.model(email=self.normalize_email(email),
                          password=password,
                          is_active=True,
                          is_staff=True,
                          is_superuser=True,
                          **extra_fields)

        user.set_password(password)
        user.save(using=self.db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(blank=False, max_length=50, default="")
    email = models.EmailField(unique=True)
    # image_profile = models.ImageField(upload_to='image_profile/', default=constants.DEFAULT_IMG)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def get_short_name(self):
        return self.name

    def is_manager(self):
        return hasattr(self, 'manager')


class Manager(User):
    class Meta:
        verbose_name = _("Gerente")
        verbose_name_plural = _("Gerentes")

    objects = UserManager()
