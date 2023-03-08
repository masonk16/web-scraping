#!/usr/bin/env/ python3
import pprint

from bs4 import BeautifulSoup
import requests

url = "https://www.audible.com/search?keywords=book&node=18573211011&pageSize=50&ref=a_search_c4_pageSize_3&pf_rd_p=1d79b443-2f1d-43a3-b1dc-31a2cd242566&pf_rd_r=68FN4HT4VR3SX6M9MTA0&pageLoadId=hkWBGfVm3NAVPAx6&creativeId=18cc2d83-2aa9-46ca-8a02-1d1cc7052e2a"

response = requests.get(url)
# pprint.pprint(response.text)

soup = BeautifulSoup(response.text, "html.parser")
names = soup.select("h3 a")
for name in names:
    print(name)


