# Crie um código em Python que teste se o site pudim está
# acessível pelo computador usado.

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('\033[1:31mErro: site inacessível.\033[0m')
else:
    print('\033[1:32mSucesso: site disponível.\033[0m')
    print(site.read())