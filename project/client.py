import requests

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


""" # POST

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
    ) """


""" # PUT

REVIEW_ID = 10
URL = f'http://127.0.0.1:8000/api/v1/reviews/{REVIEW_ID}'
REVIEW = {
  "review": "Nueva reseña 2",
  "score": 50
}

response = requests.put(URL, json=REVIEW)

if response.status_code == 200:
    print('Reseña actualizada de forma exitosa.')

    print(response.json())
else:
    print(
        response.content
    ) """


""" # DELETE

REVIEW_ID = 10
URL = f'http://127.0.0.1:8000/api/v1/reviews/{REVIEW_ID}'

response = requests.delete(URL)

if response.status_code == 200:
    print('Reseña eliminada de forma exitosa.')

    print(response.json())
else:
    print(
        response.content
    ) """


""" # GET_ID

REVIEW_ID = 9
URL = f'http://127.0.0.1:8000/api/v1/reviews/{REVIEW_ID}'

response = requests.get(URL)

if response.status_code == 200:
    print('Reseña eliminada de forma exitosa.')

    print(response.json())
else:
    print(
        response.content
    ) """


URL = f'http://127.0.0.1:8000/api/v1/users/'
USER = {
    "username": "user4",
    "password": "password4"
}

response = requests.post(URL + 'login', json=USER)

if response.status_code == 200:
    print("Usario autenticado de forma exitosa.")

    """     
    print(response.json()) # RequestsCookieJar
    print(response.cookies)
    print(response.cookies.get_dict())
    """

    user_id = response.cookies.get_dict().get('user_id')
    
    cookies = { 'user_id': user_id }
    response = requests.get(URL + 'reviews', cookies=cookies)

    if response.status_code == 200:

        for review in response.json():
            print(f"{review['review']} - {review['score']}")
else:
    print("Error de LOGIN")