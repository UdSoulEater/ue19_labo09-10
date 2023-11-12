import requests

def get_pun():
    response = requests.get('https://punapi.rest/api/pun')
    data = response.json()
    return data['pun']

if __name__ == "__main__":
    joke = get_pun()
    print(joke)
#OK    