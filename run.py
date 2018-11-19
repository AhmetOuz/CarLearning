import requests
import re
import sys
import json

print(sys.version)

url = "https://www.sahibinden.com/ilan/vasita-otomobil-bmw-axu-motors-florya-borusan-118-i-m-paket-ici-kirmizi-hafizali-584312503/detay"

saveFileFlag = 0
header = {"User-Agent": "My User-Agent 1.0", "From": "youremail@domain.com"}
r = requests.get(url, headers=header) 
content = r.text



if saveFileFlag == 1:
    try:
        file = open("source.txt", "w")
        file.write(content)
    except:
        print("Exception occured while opening or writing to file.")
    finally:
        file.close()

jsonStringList = []
regex_sequence = re.compile(
    r"<script\W+id\W*=\W*\"gaPageViewTrackingData\"\W+type\W*=\W*\"text/javascript\">\n*\W*var.*\W+=\W(.*);", re.MULTILINE)
for match in regex_sequence.finditer(content):
    jsonStringList.append(match.group(1))
    
foundJsonCount = len(jsonStringList)
if foundJsonCount > 0:
    print(str(foundJsonCount) + " Json pattern(s) found.\n")
    for item in jsonStringList:
        obj = json.loads(item)
        # print (obj)
        # print ("=="*64)
        # print (item)
else:
    print("No Json pattern found.")

myDic= {}

desiredNameList = ["km", "motor_gucu", "motor_hacmi", "renk","hasar_durumu"]
dmpDataLen = len(obj["dmpData"])
for i in range(dmpDataLen):
    for name in desiredNameList:
        if obj["dmpData"][i]["name"] == name:
            myDic[name] = obj["dmpData"][i]["value"]

print(myDic)