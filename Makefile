

build:
	sphinx-build -W --color -c docs/ -b html docs/ _build/html

serve:
	sphinx-serve

install:
	pip install -r requirements.txt

