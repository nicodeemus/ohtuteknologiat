import json
import urllib.request

with urllib.request.urlopen('https://raw.githubusercontent.com/theikkila/postinumerot/master/postcode_map_light.json') as response:
   html = (response.read())
postinrot = json.loads(html)

postitmpk = input("Kirjoita postitoimipaikka: ")
postitmpk = postitmpk.upper()

print("Postinumerot:", end =" ")

laskuri = 0

for postinro in postinrot:
    if postinrot[postinro] == postitmpk : 
        print(postinro, end=", ")
        laskuri += 1

if laskuri == 0 :
    print("Kyseisellä postitoimipaikan nimellä ei löytynyt postinumeroita")
