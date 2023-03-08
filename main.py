#!/usr/bin/env/ python3
from bs4 import BeautifulSoup
import requests

url = "https://steamdb.info/charts/"

response = requests.get(url)

