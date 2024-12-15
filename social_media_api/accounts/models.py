from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    following = models.ManyToManyField(
        'self', 
        symmetrical=False,  # Asymmetrical relationship (user A follows user B, but B does not follow A automatically)
        related_name='followers',  # The reverse relationship to get followers of a user
        blank=True  # Allow the user to have no followers initially
    )
