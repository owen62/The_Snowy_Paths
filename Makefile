install:
	python3 -m pip install --upgrade pip
	python3 -m pip install -r requirements.txt

run:
	python3 src/main.py

build-app:
	python3 -m pip install pyinstaller
	pyinstaller --onefile  src/main.py --noconsole

clean:
	rm *.spec