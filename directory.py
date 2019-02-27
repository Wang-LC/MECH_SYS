import urllib.request
import sys
from bs4 import BeautifulSoup

# install BeautifulSoup
# install lxml

base = "http://directory.oregonstate.edu/"

def main():
    input_query = sys.argv[1:]
    # input_query = ["Edward+Feser"]
    query_string = ("+".join(input_query))
    # http://directory.oregonstate.edu/?type=search&cn=Edward+Fesser
    # url = urllib.request.urlopen("http://directory.oregonstate.edu/?type=search&cn=%s" % query_string)
    
    url = base + "?type=search&cn=%s" % query_string
    soup = readSoup(url)
    isSingle = 1
    if(soup.find("h2") != None):
        isSingle = 0

    if(isSingle == 1):
        result = findSingle(soup)
        printDict(result)
    else:
        results = findMultiple(soup)
        for result in results:
            printDict(result)
            print("-" * 30)

def readSoup(url):
    web_content = urllib.request.urlopen(url)
    html = web_content.read().decode("UTF-8")
    return BeautifulSoup(html, "lxml").find(id = "records")

def findSingle(soup):
    titleList = [tag.text for tag in soup.findAll("dt")]
    infoList = [tag.text for tag in soup.findAll("dd")]
    return {titleList[i]: infoList[i] for i in range(len(titleList))}

def printDict(slist):
    for v, k in slist.items():
        print("%s: %s" % (v, k))

def findMultiple(soup):
    records = soup.find_all('a', href=True, attrs={'class':''})
    results = []
    for record in records:
        results.append(findSingle(readSoup(base + record['href'])))
    return results

if __name__ == "__main__":
    main()