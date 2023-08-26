install:
	python3 -m pip install --upgrade pip
	python3 -m pip install -r requirements.txt

run:
	python3 src/main.py

build-app:
	pyinstaller src/main.py --noconsole --add-data Icon;Icon --add-data assets;assets --icon "Icon/dragon_icon.ico"

macos-build-app:
	python3 -m pip install pyinstaller
	pyinstaller src/main.py \ 
		--noconsole \
		--add-data "Icon:Icon" \
		--icon "Icon/dragon_icon.icns"

clean:
	rm *.spec