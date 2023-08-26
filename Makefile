install:
	python3 -m pip install --upgrade pip
	python3 -m pip install -r requirements.txt

run:
	python3 src/main.py

build-windows-latest:
	pyinstaller src/main.py --onefile --noconsole  --clean --add-data Icon;Icon --add-data assets;assets --icon "Icon/dragon_icon.ico"

build-macos-latest:
	pyinstaller src/main.py --onefile --noconsole  --clean --add-data Icon:Icon --add-data assets:assets --icon "Icon/dragon_icon.icns"

build-ubuntu-latest:
	pyinstaller src/main.py --onefile --noconsole  --clean --add-data Icon:Icon --add-data assets:assets --icon "Icon/dragon_icon.ico"

clean:
	rm *.spec