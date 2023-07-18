#!/opt/homebrew/bin/python3

import requests
import json
from pathlib import Path

name='japan'
url = f'https://restcountries.com/v3.1/name/{name}'
resp = requests.get(url)
data = resp.json()

Path('response.json').write_text(json.dumps(data,indent=2,ensure_ascii=False))
# print(json.dumps(data,indent=2,ensure_ascii=False))
# breakpoint()
print(data[0]["capital"][0])