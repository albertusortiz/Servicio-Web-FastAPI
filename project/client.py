import requests
from requests.api import head

""" # GET

URL = 'http://127.0.0.1:8000/api/v1/reviews'
HEADERS = { 'accept': 'application/json' }
QUERYSET= { 'page': 1, 'limit': 2 }

response = requests.get(URL, headers=HEADERS, params=QUERYSET)

if response.status_code == 200:
    print("Peticion realizada de forma exitosa.")

    #print(response.content)
    print('\n')

    #print(response.headers)
    if response.headers.get('content-type') == 'application/json':
        
        reviews = response.json()

        for review in reviews:
            print(f'> score: {review["score"]} - {review["review"]}') """


# POST

URL = 'http://127.0.0.1:8000/api/v1/reviews'
REVIEW = {
    "user_id": 1,
    "movie_id": 1,
    "review": "Review creada con request.",
    "score": 2
}

response = requests.post(URL, json=REVIEW)

if response.status_code == 200:
    print('Reseña creada de forma exitosa.')

    print(response.json()["id"])
else:
    print(
        response.content
    )