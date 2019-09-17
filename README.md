# AireAsu
Twitter bot that tweet about the air quality in Asunción, Paraguay (work in progress)

## Requirements

* Python 3.6+
* BeautifulSoup4
* Chromium Webdriver

## Prerequisites
You can download the Chromium Webdriver from https://chromedriver.chromium.org/downloads or install via package manager.

### Ubuntu
```bash
sudo apt install chromium-chromedriver
```

### Arch/Manjaro
```bash
sudo pacman -S chromium
```

## Install

```
git clone git@github.com:melizeche/AireAsu.git
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python airdata.py
```
### Crontab format and example

MIN 	HOUR 	DAYofMONTH 	MONTH 	DAYofWEEK 	PYTHONPATH SCRIPT

 For check and tweet  at 8:10am, 12:10pm and 6:10pm everyday

```0      8,12,18    * * * /apps/AireAsu/env/bin/python /apps/AireAsu/airdata.py```

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## Disclaimer

This project use public data from http://mediciones.aire.uc.edu.py and https://www.airvisual.com/paraguay/asuncion but is not asociated with any of them.


## Author

* Marcelo Elizeche Landó https://github.com/melizeche

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.
