from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(max_length=100)
    location = models.CharField(max_length=100)
    is_admin = models.BooleanField(default=False)
    is_banned = models.BooleanField(default=False)
    url = models.CharField(max_length=200, blank=True, default=False)
    
class Route(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=6)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="route")
    description = models.CharField(max_length=2200)
    url = models.CharField(max_length=200, blank=True, null=True)
    climb_type = models.CharField(max_length=30)
    pitch = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.name

class Review(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="review")
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name="review")
    rating = models.DecimalField(
        max_digits=2, 
        decimal_places=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
    content = models.CharField(max_length=1250)
    posted_at = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="like")
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="like")