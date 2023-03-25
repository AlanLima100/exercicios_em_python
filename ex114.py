# CRIE UM CÓDIGO EM pYTHON QUE TESTE SE O SITE PDUIM ESTÁ ACESSÍVEL PELO COMPUTADOR USADO.

import urllib
import urllib.request


try:
    site = urllib.request.urlopen("http://www.pudim.com.br")
except urllib.error.URLError:
    print("O site Pudim não está acessível no momento")
else:
    print("Consegui acessar o site Pudim com sucesso!")

