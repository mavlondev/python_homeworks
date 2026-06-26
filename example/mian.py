from core.to_json import write_file
from core.detail_def import *
import requests
from bs4 import BeautifulSoup


if __name__ == "__main__":
    # write_file([
    #     {'id':1, "fname":"Mavlon"}, 
    #     {"id":2, "fname":"Sardor"}
    # ])

    # print(avarage(2, 3, 4, 5, 2, 1))
    site = requests.get("http://127.0.0.1:5500/example/index.html")
    soup = BeautifulSoup(site.content, "html.parser")
    for item in soup.find_all("tr"):
        print(item.text)