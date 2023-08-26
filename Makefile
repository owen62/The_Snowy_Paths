install:
	python3 -m pip install --upgrade pip
	python3 -m pip install -r requirements.txt

run:
	python3 src/main.py

build-windows-latest:
	pyinstaller src/main.py --onefile --noconsole  --clean --add-data "icon;icon" --add-data "assets;assets" --icon "Icon/dragon_icon.ico" --add-data music;music

build-macos-latest:
	pyinstaller src/main.py --onefile --noconsole  --clean --add-data icon:icon --add-data assets:assets --icon "Icon/dragon_icon.icns" --add-data music:music

build-ubuntu-latest:
	pyinstaller src/main.py --onefile --noconsole  --clean --add-data icon:icon --add-data assets:assets --icon "Icon/dragon_icon.ico" --add-data music:music

clean:
	rm *.spec