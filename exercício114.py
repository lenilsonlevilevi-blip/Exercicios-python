import urllib
import urllib.request
try:
    site = urllib.request.urlopen('http://www.google.com')
except Exception as erro:
    print(f'erro encontrado: {erro}')
else:
    print('Consegui acessar o site no momento ')