import tweepy
import requests
from datetime import datetime
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
            self.legend = "👍 Bueno"
            self.img = f"images/{self.source}0.png"
        elif self.index < 101:
            self.legend = "😐 Moderado"
            self.img = f"images/{self.source}1.png"
        elif self.index < 151:
            self.legend = "⚠😷️👶💔👴🤰 Insalubre para grupos sensibles"
            self.img = f"images/{self.source}2.png"
        elif self.index < 201:
            self.legend = "⚠😷‼️ Insalubre"
            self.img = f"images/{self.source}3.png"
        elif self.index < 301:
            self.legend = "☣️☣️☣️ Muy Insalubre"
            self.img = f"images/{self.source}4.png"
        else:
            self.legend = "☠️☠️☠️ Peligroso"
            self.img = f"images/{self.source}5.png"


def get_uca():
    global updated
    soup = BeautifulSoup(
        requests.get(
            UCA_URL, timeout=10, headers={"user-agent": "Mozilla/5.0"}, verify=False
        ).text,
        "html.parser",
    )
    ica_index = float(soup.find(class_="button white").text.split("(")[1].split(")")[0])
    updated = soup.findAll("strong")[1].text
    return ica_index


def get_airvisual():
    soup = BeautifulSoup(
        requests.get(
            AIRVISUAL_URL, timeout=10, headers={"user-agent": "Mozilla/5.0"}
        ).text,
        "html.parser",
    )
    aqi_index = float(soup.find(class_="aqi").contents[0])
   

    return aqi_index


def build_text():
    global uca
    global airvisual
    #global updated #meanwhile mediciones UC is not updating
    updated = datetime.now().strftime("%d/%b/%Y, %H:%M")
    text = f"""===AireAsu Bot===
#AireAsunción

Índice de Calidad de Aire PM2,5:
{uca.index} - {uca.legend} 
{UCA_URL} 

Air Quality Index US:
{airvisual.index} - {airvisual.legend}
{AIRVISUAL_URL}

Última actualización: {updated}"""
    return text


def tweet(msg, images=[], reply_id=None):
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)
    media_ids = [api.media_upload(i).media_id_string for i in images]
    if reply_id:
        result = api.update_status(status=msg, media_ids=media_ids, in_reply_to_status_id=reply_id)
    else:
        result = api.update_status(status=msg, media_ids=media_ids)
    with open("last_tweet","w") as f:
        f.write(result.id_str)
    print(result.id_str)



if __name__ == "__main__":
    updated=""
    reply_id = None
    uca = AirQuality(get_uca(), "uc")
    airvisual = AirQuality(get_airvisual(), "av")
    print(build_text())
    print(uca.img, airvisual.img)
    map = get_screenshot()
    print(map, type(map), map._str)
    try:
        with open("last_tweet","r") as f:
            reply_id = f.readline()
    except:...

    tweet(msg=build_text(), images=[map._str, uca.img, airvisual.img],reply_id=reply_id)

