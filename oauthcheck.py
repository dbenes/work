import requests

def get_access_token(client_id, client_secret, token_url):
    data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'client_credentials'
    }

    response = requests.post(token_url, data=data)
    print("Response Status Code:", response.status_code)
    print("Response Content:", response.content)

    if response.status_code == 200:
        return response.json().get('access_token')
    else:
        print(f"Failed to get access token: {response.text}")

if __name__ == "__main__":
    client_id = input("Enter your client ID: ")
    client_secret = input("Enter your client secret: ")
    token_url = 'http://localhost:5000/oauth/token'  # Update if your server is hosted elsewhere

    access_token = get_access_token(client_id, client_secret, token_url)
    print("Access token:", access_token)
