import requests
from bs4 import BeautifulSoup

url = "http://www.saramin.co.kr/zf_user/search/recruit?search_area=main&search_done=y&search_optional_item=n&searchType=search&searchword=Python"


def saramin_page():
    get_request = requests.get(url)
    get_soup = BeautifulSoup(get_request.text, "html.parser")
    find_pages = get_soup.find("div", {"pagination"}).find_all("a")
    last_page = find_pages[-2].get_text(strip=True)

    return int(last_page)


def saramin_scrap():
    pass


def saramin_main():

    start = saramin_page()

