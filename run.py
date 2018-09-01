import requests


header = {"User-Agent": "My User-Agent 1.0", "From": "youremail@domain.com"}
r = requests.get(
    'https://www.sahibinden.com/ilan/vasita-otomobil-bmw-auto-reza-2012-bmw-640d-grand-coupe-distronic-head-up-masaj-600139580/detay', headers=header)
content = r.text

try:
    file = open("source.txt", "w")
    file.write(content)
except:
    print("Exception occured while opening or writing to file.")
finally:
    file.close()
