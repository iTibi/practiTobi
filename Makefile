build:
	pip install prettytable
	python -m compileall .

clean:
	rd /q /s __pycache__

install:
	IF NOT EXIST "\path" (md \path);
	copy . \path