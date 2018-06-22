import requests

result=requests.get('https://api.github.com/users/shiveshabhishek')

print(result.text)
