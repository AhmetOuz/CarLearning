import requests
import re

saveFileFlag = False
header = {"User-Agent": "My User-Agent 1.0", "From": "youremail@domain.com"}
r = requests.get(
    'https://www.sahibinden.com/ilan/vasita-otomobil-bmw-auto-reza-2012-bmw-640d-grand-coupe-distronic-head-up-masaj-600139580/detay', headers=header)
content = r.text


if saveFileFlag:
    try:
        file = open("source.txt", "w")
        file.write(content)
    except:
        print("Exception occured while opening or writing to file.")
    finally:
        file.close()

jsonStringList = []
regex_sequence = re.compile(
    r"<script\W+id\W*=\W*\"gaPageViewTrackingData\"\W+type\W*=\W*\"text/javascript\">\n*\W*var.*=(.*);", re.MULTILINE)
for match in regex_sequence.finditer(content):
    jsonStringList.append(match.group(1)),

foundJsonCount = len(jsonStringList)
if foundJsonCount > 0:
    print(str(foundJsonCount) + " Json pattern(s) found.\n")
    for item in jsonStringList:
        print(item)
else:
    print("No Json pattern found.")
