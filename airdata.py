import tweepy
import requests
from bs4 import BeautifulSoup
from screen import get_screenshot
from config import ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET


UCA_URL = "http://mediciones.aire.uc.edu.py"
AIRVISUAL_URL = "https://www.airvisual.com/paraguay/asuncion"


class AirQuality:
    def __init__(self, an_index, source):
        self.index = an_index
        self.source = source

        if self.index < 51:
            self.legend = "Bueno"
            self.img = "0.png"
        elif self.index < 101:
            self.legend = "Moderado"
            self.img = "1.png"
        elif self.index < 151:
            self.legend = "Insalubre para grupos sensibles"
            self.img = "2.png"
        elif self.index < 201:
            self.legend = "Insalubre"
            self.img = "3.png"
        elif self.index < 301:
            self.legend = "Muy Insalubre"
            self.img = "4.png"
        else:
            self.legend = "Peligroso"
            self.img = "5.png"


def get_uca():
    soup = BeautifulSoup(
        requests.get(
            UCA_URL, timeout=10, headers={"user-agent": "Mozilla/5.0"}, verify=False
        ).text,
        "html.parser",
    )
    ica_index = float(soup.find(class_="button white").text.split("(")[1].split(")")[0])
    ica_legend = soup.find(class_="button white").text.split("(")[0].strip()

    return {"index": ica_index, "legend": ica_legend}


def get_airvisual():
    soup = BeautifulSoup(
        requests.get(
            AIRVISUAL_URL, timeout=10, headers={"user-agent": "Mozilla/5.0"}
        ).text,
        "html.parser",
    )
    aqi_index = float(soup.find(class_="aqi").contents[0])
    aqi_legend = soup.find(class_="status-text").text

    return {"index": aqi_index, "legend": aqi_legend}


def build_text():
    uca = get_uca()
    airvisual = get_airvisual()
    text = f"""Índice de Calidad de Aire PM2,5:
{uca["index"]} - {uca["legend"]} 
{UCA_URL} 
Air Quality Index US:
{airvisual["index"]} - {airvisual["legend"]}
{AIRVISUAL_URL}"""
    return text


def tweet(msg):
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)
    images = ("image1.png", "image2.png")
    media_ids = [api.media_upload(i).media_id_string for i in images]
    api.update_status(status=msg, media_ids=media_ids)


if __name__ == "__main__":
    # print(get_uca())
    # print(get_airvisual())
    print(build_text())

