import requests
from bs4 import BeautifulSoup

url = "http://www.saramin.co.kr/zf_user/search/recruit?search_area=main&search_done=y&search_optional_item=n&searchType=search&searchword=Python"

get_request = requests.get(url)
get_soup = BeautifulSoup(get_request.text, "html.parser")
print(get_soup)
