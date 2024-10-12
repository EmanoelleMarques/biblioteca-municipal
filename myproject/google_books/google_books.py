import requests


def search_books(query):
    api_key = "AIzaSyByWziaFvBglInl1bvv-0nZKi2R97qflow"
    url = f"https://www.googleapis.com/books/v1/volumes?q={query}&key={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None
