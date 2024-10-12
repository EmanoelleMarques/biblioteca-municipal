from django.shortcuts import render
from .google_books import search_books


def book_search(request):
    results = []
    if "query" in request.GET:
        query = request.GET["query"]
        results = search_books(query)

    return render(request, "books/search_results.html", {"results": results})
