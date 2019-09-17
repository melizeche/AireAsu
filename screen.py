# Ubuntu: apt install chromium-chromedriver
# Arch/Manjaro: pacman -S chromium 

from selenium import webdriver
import time
from datetime import datetime
from PIL import Image

URL = "https://www.airvisual.com/air-quality-map?lat=-23.60066&lng=-58.23591&zoomLevel=7"

# Headless Chrome/Selenium setup
options = webdriver.ChromeOptions()
options.add_argument("headless")
options.add_argument("disable-infobars")  # disabling infobars
options.add_argument("--disable-extensions")  # disabling extensions
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")  # Bypass OS security model
# Thanks to https://stackoverflow.com/a/50642913/2291648 for explaining the arguments above

timestamp_str = datetime.now().strftime("%b%d-%H")
screenshot_filename = f"screen_{timestamp_str}.png" 

with webdriver.Chrome(options=options) as driver:
    driver.set_window_size(1920,900)
    driver.get(URL)
    time.sleep(4)
    driver.save_screenshot(screenshot_filename)

im = Image.open(screenshot_filename)
#Set box coordinates to crop
left, top, right, bottom = 542, 0, 1346, 900
cropped_img = im.crop((left,top,right,bottom))
cropped_img.save(screenshot_filename)

