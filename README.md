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
sudo apt install chromium-webdriver
git clone git@github.com:melizeche/AireAsu.git
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## Author

* Marcelo Elizeche Landó https://github.com/melizeche

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details