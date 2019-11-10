from urllib import request
from bs4 import BeautifulSoup


def dmx_status() -> (str, bool):
    url = "http://isdmxinjail.com/"
    soup = BeautifulSoup(request.urlopen(url).read().decode('UTF-8'), features="html.parser")
    status = soup.find("div", {"id":"main"}).text.strip()
    if "not" in status:
        jail = False
    else:
        jail = True
    return status, jail

