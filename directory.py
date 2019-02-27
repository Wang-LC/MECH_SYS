import urllib.request
import sys
from bs4 import BeautifulSoup

# install BeautifulSoup
# install lxml

def main():
    # Single content
    input_query = sys.argv[1:]
    # input_query = ["Edward+Feser"]
    query_string = ("+".join(input_query))
    
    # http://directory.oregonstate.edu/?type=search&cn=Edward+Fesser
    web_content = urllib.request.urlopen("http://directory.oregonstate.edu/?type=search&cn=%s" % query_string)
    html = web_content.read().decode("UTF-8")

    soup = BeautifulSoup(html, "lxml").find(id = "records")
    titleList = [tag.text for tag in soup.findAll("dt")]
    infoList = [tag.text for tag in soup.findAll("dd")]
   
    #print(soup)
    for i in range(len(titleList)):
        print("%s: %s" % (titleList[i], infoList[i]))

    # print(titleList)
    # print(infoList)

if __name__ == "__main__":
    main()