# https://mime.oregonstate.edu/people
# -*- coding: utf-8 -*-
# ！/usr/bin/env python
import urllib
from bs4 import BeautifulSoup


def mime_count():
    url = "https://mime.oregonstate.edu/people"
    content = readContent(url)
    jobs = {}
    for row in content.tbody.findAll('tr'):
        job_title = row.findAll('td')[2].text.split('\n')
        for item in job_title:
            if item not in jobs:
                jobs[item] = 0
            jobs[item] += 1
    del jobs[""]
    print_func(jobs)


def print_func(jobs):
    for key, value in jobs.items():
        print("%s: %s" % (key, value))


def readContent(url):
    web_content = urllib.request.urlopen(url)
    html = web_content.read().decode("UTF-8")
    soup = BeautifulSoup(html, "lxml")
    content = soup.findAll("table", attrs={'class': 'views-table'})[0]
    return content


if __name__ == "__main__":
    mime_count()
