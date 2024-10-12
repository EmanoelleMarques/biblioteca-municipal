from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    thumbnail = models.URLField(null=True, blank=True)
    published_date = models.CharField(max_length=10, null=True, blank=True)
    google_books_id = models.CharField(max_length=100, unique=True)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.title
