from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from .book import Book

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews_created")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="books_reviewed")
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    comment = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    