#verificar se o site www.pudim.com.br está acessível
import urllib
import urllib.request
try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLerror:
    print('Site não acessível no nomento!')
else:
    print('Consegui acessar o site com sucesso!')
#se eu quiser ler o site todo posso usar site.read()

