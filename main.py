#!/usr/bin/env/ python3
import csv
import pprint
from itertools import zip_longest
from bs4 import BeautifulSoup
import requests

url = "https://www.audible.com/search?keywords=book&node=18573211011&pageSize=50&ref=a_search_c4_pageSize_3&pf_rd_p=1d79b443-2f1d-43a3-b1dc-31a2cd242566&pf_rd_r=68FN4HT4VR3SX6M9MTA0&pageLoadId=hkWBGfVm3NAVPAx6&creativeId=18cc2d83-2aa9-46ca-8a02-1d1cc7052e2a"

response = requests.get(url)

# Instantiate Beautiful Soup
soup = BeautifulSoup(response.text, "html.parser")

# Scrape Data
book_names = soup.select("h3 a")
runtimes = soup.select("[class~=runtimeLabel] > span")
release_dates = soup.select("[class~=releaseDateLabel] > span")
languages = soup.select("[class~=languageLabel] > span")
prices = soup.select("[class~=buybox-regular-price] > span:nth-of-type(2)")

# Extract text  and clean data
clean_book_names = [book_name.get_text() for book_name in book_names]
clean_runtimes = [runtime.get_text().split(":")[1].strip() for runtime in runtimes]
clean_release_dates = [release_date.get_text().split(":")[1].strip() for release_date in release_dates]
clean_languages = [language.get_text().split(":")[1].strip() for language in languages]
clean_prices = [price.get_text(strip=True) for price in prices]

# # Create csv file
# with open('computers-and-technology-audiobooks.csv', 'w') as file:
#     writer = csv.writer(file)
#     writer.writerow(["Book Name", "Length" "Release Date", "Language", "Price"])
#     for row in zip_longest(clean_book_names, clean_runtimes, clean_release_dates, clean_languages, clean_prices):
#         writer.writerow(row)
