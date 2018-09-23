CWD=$(shell pwd)
ENV=$(CWD)/venv

$(ENV):
	virtualenv -p python3.4 $(ENV)

.pip: $(ENV)
	$(ENV)/bin/pip3 install -r requirements.txt

