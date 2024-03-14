#esempi di utilizzo della libreria requests per accedere al contenuto delle pagine web
import requests

url = 'https://www.google.com'
response = requests.get(url)
print(response.text)
print(response.status_code)
print(response.headers)
