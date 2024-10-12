import requests
from django.shortcuts import render
from .models import Book
from .views import fetch_books_from_google

