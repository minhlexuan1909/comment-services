from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Comment(models.Model):
    account_id = models.IntegerField()
    product_id = models.IntegerField()
    user_name = models.CharField(max_length=255)
    star_rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment {self.id} - {self.user_name}"
