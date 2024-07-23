### install dependencies

pip install -r requirements.txt

### Start project
python main.py

### How to build exe file 
pyinstaller --onefile --windowed --add-binary "chromedriver.exe;." main.py


pyinstaller --onefile main-switcher.py
pyinstaller --onefile main.py

pyinstaller main-switcher.spec
