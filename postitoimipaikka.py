import json
import urllib.request

with urllib.request.urlopen('https://raw.githubusercontent.com/theikkila/postinumerot/master/postcode_map_light.json') as response:
   html = (response.read())
postinrot = json.loads(html)

postinro = input("Kirjoita postinumero: ")

print(postinrot[postinro])
