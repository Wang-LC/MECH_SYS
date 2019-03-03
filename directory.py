import urllib.request
import sys
from bs4 import BeautifulSoup
# install BeautifulSoup
# install lxml


base = "http://directory.oregonstate.edu/"


class people:
    def __init__(self, name, title, department, phone):
        self.name = name
        self.title = title
        self.department = department
        self.phone = phone

    def pprint(self):
        # ---------------------------------------
        # Name: Feser, Edward
        # Title: Executive 1-Provost/Exec VP
        # Department: Provost / Exec Vice Pres
        # Phone: 123-123-4321
        # ---------------------------------------
        print("Name: %s\nTitle: %s\nDepartment: %s\nPhone: %s\n" % (self.name, self.title, self.department, self.phone))


def main():  # before main() raise ValueError('Please enter a name')
    input_name = sys.argv[1:]
    # input_name = ["Edward+Feser"]
    name_string = ("+".join(input_name))
    # http://directory.oregonstate.edu/?type=search&cn=Edward+Fesser
    
    url = base + "?type=search&cn=%s" % name_string
    soup = readSoup(url).find(id="records")
    # deal with too many returns shown on the website
    if soup is None:
        soup = readSoup(url).find("body")
        print(soup.find('h2').text)
        exit()

    isSingle = 1
    # is multiple people
    if soup.find("h2") is not None:
        isSingle = 0

    if isSingle == 1:
        result = findSingle(soup)
        result.pprint()
    else:
        results = findMultiple(soup)
        for result in results:
            result.pprint()
            print("-" * 30)


def readSoup(url):  # read html part by id readSoup().find()
    web_content = urllib.request.urlopen(url)
    html = web_content.read().decode("UTF-8")
    return BeautifulSoup(html, "lxml")


def findSingle(soup):  # find person info
    titleList = [tag.text for tag in soup.find_all("dt")]
    infoList = [tag.text for tag in soup.find_all("dd")]
    infoDict = {titleList[i]: infoList[i] for i in range(len(titleList))}
    # only need four info
    name = infoDict["Full Name"]
    try:
        title = infoDict["Primary Affiliation"]
    except KeyError:
        title = ""

    try:
        department = infoDict["Department"]
    except KeyError:
        department = ""

    try:
        phone = infoDict["Office Phone Number"]
    except KeyError:
        phone = ""

    return people(name, title, department, phone)


def findMultiple(soup):  # deal with multiple person and no this name
    records = soup.find_all('a', href=True, attrs={'class': ''})
    results = []
    if not records:  # no this name
        print(soup.find('h2').text)
        exit()
    else:
        for record in records:
            results.append(findSingle(readSoup(base + record['href'])))
        return results


def mime_count():
    url = "https://mime.oregonstate.edu/people"
    content = readContent(url)
    # set job dictionary
    jobs = {}
    for row in content.tbody.findAll('tr'):
        job_title = row.findAll('td')[2].text.split('\n')
        for item in job_title:
            if item not in jobs:  # set a new job key
                jobs[item] = 0
            jobs[item] += 1
    del jobs[""]
    for key, value in jobs.items():
        print("%s: %s" % (key, value))


def readContent(url):
    web_content = urllib.request.urlopen(url)
    html = web_content.read().decode("UTF-8")
    soup = BeautifulSoup(html, "lxml")
    content = soup.findAll("table", attrs={'class': 'views-table'})[0]
    return content


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise ValueError('Please enter a name')
    else:
        main()
