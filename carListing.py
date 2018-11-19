import requests
import re
import sys
import json

print(sys.version)

url = "https://www.sahibinden.com/audi-a3?pagingSize=50"
saveFileFlag = True
debugFlag = False
hasNext = True
header = {"User-Agent": "My User-Agent 1.0", "From": "youremail@domain.com"}
linkList = []
pageList = []
findLinksSequence = re.compile(r"<a\W+class\W*=\W*\"\W*classifiedTitle\W*\"\W+href\W*=\W*\"(.*)\"\W*>", re.MULTILINE)
nextPageSequence = re.compile(r"<div class=\"pageNavTable\">.*<a href=\"(.*)\" class=\"prevNextBut\">.*</a>.*</div>", re.MULTILINE|re.DOTALL)
file = open("carlist.txt", "w")

while hasNext == True:
    hasNext = False
    r = requests.get(url, headers=header) 
    content = r.text

    for match in findLinksSequence.finditer(content):
        
        linkList.append(match.group(1))
        if saveFileFlag == 1:
            file.write("https://www.sahibinden.com" + match.group(1) +"\n")

    file.flush()
            # print("File written successfully ;))")

    if debugFlag == 1:
        linkCount = len(linkList)
        if linkCount > 0:
            print("\n" + str(linkCount) + " Link(s) found.\n")
        else:
            print("No links found.")

    #save file
   

    #next page
    for match in nextPageSequence.finditer(content):
        pageList.append(match.group(1))
        print(pageList)
        url = "https://www.sahibinden.com" + match.group(1)
        hasNext = True



    
print (len(linkList))
file.close()
