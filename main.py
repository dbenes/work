from flask import Flask, request, jsonify

app = Flask(__name__)

# Load client credentials from file
def load_client_credentials(filename):
    with open(filename, 'r') as file:
        credentials = {}
        for line in file:
            parts = line.strip().split('=')
            if len(parts) == 2:
                key, value = parts
                credentials[key] = {'client_id': key, 'client_secret': value}
            else:
                print(f"Ignoring line: {line.strip()} as it does not contain valid data.")
        return credentials

CLIENTS = load_client_credentials('client_credentials.txt')

@app.route('/oauth/token', methods=['POST'])
def token():
    client_id = request.form.get('client_id')
    client_secret = request.form.get('client_secret')
    grant_type = request.form.get('grant_type')

    if not client_id or not client_secret or grant_type != 'client_credentials':
        return jsonify({'error': 'invalid_request', 'description': 'Invalid client credentials or grant type'}), 400

    if CLIENTS.get(client_id) and CLIENTS[client_id]['client_secret'] == client_secret:
        # In a real-world scenario, you would generate a unique access token here
        access_token = 'ACCESS GRANTED!'
        return jsonify({'access_token': access_token, 'token_type': 'bearer', 'expires_in': 3600}), 200
    else:
        return jsonify({'error': 'invalid_client', 'description': 'Invalid client credentials'}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
