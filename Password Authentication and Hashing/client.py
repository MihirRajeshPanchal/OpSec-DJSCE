import requests

server_url = 'http://localhost:5000'  

def register(username, password):
    response = requests.post(f'{server_url}/register', json={'username': username, 'password': password})
    return response.json()

def login(username, password):
    response = requests.post(f'{server_url}/login', json={'username': username, 'password': password})
    return response.json()

if __name__ == '__main__':
    
    print(register('user1', 'password1'))
    print(login('user1', 'password1'))
