# Ubuntu: apt install chromium-chromedriver
# Arch/Manjaro: pacman -S chromium 
import time
from selenium import webdriver
from datetime import datetime
from PIL import Image
from pathlib import Path

URL = "https://www.airvisual.com/air-quality-map?lat=-23.60066&lng=-58.23591&zoomLevel=7"

SCREENSHOTS_DIR = Path.cwd().joinpath('screenshots')
if not SCREENSHOTS_DIR.exists():
    SCREENSHOTS_DIR.mkdir()

def get_screenshot():
    # Headless Chrome/Selenium setup
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    options.add_argument("disable-infobars")  # disabling infobars
    options.add_argument("--disable-extensions")  # disabling extensions
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")  # Bypass OS security model
    # Thanks to https://stackoverflow.com/a/50642913/2291648 for explaining the arguments above

    timestamp_str = datetime.now().strftime("%b%d-%H")
    screenshot_path = SCREENSHOTS_DIR.joinpath(f"screen_{timestamp_str}.png")
    print(screenshot_path)
    try:
        with webdriver.Chrome(options=options) as driver:
            driver.set_window_size(1920,900)
            driver.get(URL)
            time.sleep(4)
            driver.save_screenshot(screenshot_path._str)

        im = Image.open(screenshot_path)
        # Set box coordinates to crop (in pixels)
        left, top, right, bottom = 542, 0, 1346, 900
        cropped_img = im.crop((left,top,right,bottom))
        cropped_img.save(screenshot_path)
    except Exception as e:
        print(type(e),e)
        return False

    return True

if __name__ == "__main__" :
    get_screenshot()
