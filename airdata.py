import requests
from bs4 import BeautifulSoup

UCA_URL = "http://mediciones.aire.uc.edu.py"
AIRVISUAL_URL = "https://www.airvisual.com/paraguay/asuncion"


def get_uca():
    soup = BeautifulSoup(
        requests.get(
            UCA_URL, timeout=10, headers={"user-agent": "Mozilla/5.0"}, verify=False
        ).text,
        "html.parser",
    )
    ica_index = float(soup.find(class_="button white").text.split('(')[1].split(')')[0])
    ica_legend = soup.find(class_="button white").text.split('(')[0].strip()

    return {"index":ica_index, "legend":ica_legend}

def get_airvisual():
    soup = BeautifulSoup(
        requests.get(
            AIRVISUAL_URL, timeout=10, headers={"user-agent": "Mozilla/5.0"}).text,
        "html.parser",
    )
    ica_index = float(soup.find(class_="aqi").contents[0])
    ica_legend = soup.find(class_="status-text").text

    return {"index":ica_index, "legend":ica_legend}


if __name__=="__main__":
    print(get_uca())
    print(get_airvisual())



