# https://mime.oregonstate.edu/people
import urllib
from bs4 import BeautifulSoup


def mime_count():
    url = "https://mime.oregonstate.edu/people"
    content = readContent(url)
    jobs = {}
    for row in content.tbody.find_all('tr'):  # read each people job
        job_title = row.findAll('td')[2].text.split('\n')
        for item in job_title:  # count number
            if item not in jobs:
                jobs[item] = 0
            jobs[item] += 1
    # delete unused value
    del jobs[""]
    print_func(jobs)


def readContent(url):
    web_content = urllib.request.urlopen(url)
    html = web_content.read().decode("UTF-8")
    soup = BeautifulSoup(html, "lxml")
    content = soup.findAll("table", attrs={'class': 'views-table'})[0]
    return content


def print_func(jobs):
    # Assistant Professor: 21
    # Associate Professor: 12
    # ...
    for key, value in jobs.items():
        print("%s: %s" % (key, value))


if __name__ == "__main__":
    mime_count()
