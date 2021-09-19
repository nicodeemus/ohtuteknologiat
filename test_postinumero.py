import json
import urllib.request

def etsi_postinumero (postitmpk):

    with urllib.request.urlopen("https://raw.githubusercontent.com/theikkila/postinumerot/master/postcode_map_light.json") as response:
        html = (response.read())
    postinrot = json.loads(html)

    postitmpk = postitmpk.upper()
    postitmpk = postitmpk.replace("-", "")
    postitmpk = postitmpk.replace(" ", "")

    toimipaikat = ryhmittele_toimipaikoittain(postinrot)

    if postitmpk in toimipaikat:
        return toimipaikat[postitmpk]
        


def ryhmittele_toimipaikoittain(numero_sanakirja):
    paikat = {}
    for numero, nimi in numero_sanakirja.items():
        nimi = nimi.replace("-", "")
        nimi = nimi.replace (" ", "")
        if nimi not in paikat:
            paikat[nimi] = []

        paikat[nimi].append(numero)

    return paikat    


def test_zipcodeListNotEmpty():
    postinumerolista = etsi_postinumero ("helsinki")
    assert postinumerolista != []

def test_moreThanOneZipcodes():
    postinumerolista = etsi_postinumero ("helsinki")
    assert len(postinumerolista)>1

def test_randomSizedLetters():
    postinumerolista = etsi_postinumero ("hElSiNkI")
    assert postinumerolista != []

def test_spaces():
    postinumerolista = etsi_postinumero ("Rova-niemi")
    assert postinumerolista != []

def test_smartpostSeachesSmartPost():
    postinumerolista = etsi_postinumero ("SMARTPOST")
    postinumerolistaVaaraMuoto = etsi_postinumero ("Smart Post")
    assert  postinumerolista == postinumerolistaVaaraMuoto

def test_smartpostSeachesSmartPsot():
    postinumerolista = etsi_postinumero ("SMARTPOST")
    postinumerolistaVaaraMuoto = etsi_postinumero ("SMARTPSOT")
    assert  postinumerolista == postinumerolistaVaaraMuoto

def test_smartpostSeachesSmartDashPost():
    postinumerolistaVaaraMuoto = etsi_postinumero ("SMART-POST")
    postinumerolista = etsi_postinumero ("SMARTPOST")
    assert  postinumerolista == postinumerolistaVaaraMuoto

def test_smartpostSeachesSmartDashPost():
    postinumerolistaVaaraMuoto = etsi_postinumero ("SMART-POST")
    postinumerolistaVaaraMuoto2 = etsi_postinumero ("SMART POST")
    assert  postinumerolistaVaaraMuoto == postinumerolistaVaaraMuoto2
