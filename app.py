import requests

def get_pun():
    response = requests.get('https://api.punapi.com/random')
    data = response.json()
    return data['content']

if __name__ == "__main__":
    joke = get_pun()
    print(joke)
