from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "authors", "published_date", "availability")
    search_fields = ("title", "authors")


# Ou você pode usar este formato mais simples:
# admin.site.register(Book)
