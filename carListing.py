import requests
import re
import sys
import json

print(sys.version)

url = "https://www.sahibinden.com/audi-a3?pagingSize=50"

saveFileFlag = 0
header = {"User-Agent": "My User-Agent 1.0", "From": "youremail@domain.com"}
r = requests.get(url, headers=header) 
content = r.text

linkList = []
regex_sequence = re.compile(
    r"<a\W+class\W*=\W*\"\W*classifiedTitle\W*\"\W+href\W*=\W*\"(.*)\"\W*>", re.MULTILINE)
for match in regex_sequence.finditer(content):
    linkList.append(match.group(1))
    
linkCount = len(linkList)
if linkCount > 0:
    # for item in linkList:
        # obj = json.loads(item)
        # print (obj)
        # print ("=="*64)
    	# print (item)    
    print("\n" + str(linkCount) + " Link(s) found.\n")
else:
	print("No links found.")

nextPage_sequence = re.compile(r"<div class=\"pageNavTable\">.*<a href=\"(.*)\" class=\"prevNextBut\">.*</a>.*</div>", re.MULTILINE|re.DOTALL)
for match in nextPage_sequence.finditer(content):
	print(match.group(0))
	print("_$"*105)