from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
    ACTIVE = 'active'
    DELETED = 'deleted'


    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    is_admin = models.BooleanField(default=False)
    status = models.CharField(
        max_length=20,
        choices= (
            (ACTIVE, 'Active'),
            (DELETED, 'Deleted')
        ),
        default=ACTIVE
    )

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name
