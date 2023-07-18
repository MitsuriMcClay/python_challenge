#!/opt/homebrew/bin/python3

import requests
from bs4 import BeautifulSoup

resp = requests.get('https://eiga.com/movie-area/83919/13/130201/')
soup = BeautifulSoup(resp.text, 'html.parser')

breakpoint()

print(resp)