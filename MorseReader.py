# -----------------------------------------------------------
# Skripti morse-koodin lukemiseen kuvasta.
# Lukee kuvasta joka toisen rivin pikseli kerrallaan ja havaitsee siitä morse-koodin. 
# -----------------------------------------------------------

from PIL import Image
import zipfile
import shutil
import os

CODE = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' 
        }

CODE_REVERSED = {value:key for key,value in CODE.items()}

# Stringistä morseksi (ei käytetä)
def to_morse(s):
    return ' '.join(CODE.get(i.upper()) for i in s)
# Morse-stringistä kirjaimiksi tai luvuiksi
def from_morse(s):
    return ''.join(CODE_REVERSED.get(i) for i in s.split())

# Lukee morse-koodin kuvasta ja palauttaa siitä muodostuvan salasanan tavumuodossa.
def morse_kuvasta(mikakuva):
    kuva = Image.open("LISÄÄ KUVAN POLKU".format(mikakuva))
    px = kuva.load()
    viivan_pituus = 0 
    taulukko = []
    leveys, korkeus = kuva.size
    salasana = ""

    # Käy läpi pikseli kerrallaan joka toisen rivin ja laittaa taulukkoon (viivana tai pisteenä), jos eri värinen kuin pohja
    for j in range(1, korkeus, 2):
        for i in range(0, leveys):
            piste = px[i, j]
            if piste != px[0, 1]:
                viivan_pituus += 1
            else:
                if viivan_pituus == 1:
                    taulukko.append(".")
                viivan_pituus = 0
                continue
            if viivan_pituus == 3:
                taulukko.append("-")
            if viivan_pituus == 2:
                continue
        stringi = ''.join(taulukko)
        salasana += from_morse(stringi)
        taulukko.clear()

    return bytes(salasana.lower(), 'utf-8')
 