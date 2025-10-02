import requests

resposta = requests.get('https://www.google.com.br')
print(resposta.status_code)