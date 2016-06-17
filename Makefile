TOP := $(realpath .)
VENV_DIR = $(TOP)/venv

all: setup-pip
	env PATH=$(VENV_DIR)/bin:$(PATH) pip install -e .

venv:
	virtualenv $(VENV_DIR)
	env PATH=$(VENV_DIR)/bin:$(PATH) pip install --upgrade pip==8.1.1 # needed for pip-tools<1.7
	env PATH=$(VENV_DIR)/bin:$(PATH) pip install pip-tools

requirements.txt: venv requirements.in
	env PATH=$(VENV_DIR)/bin:$(PATH) $(VENV_DIR)/bin/pip-compile

setup-pip: requirements.txt
	env PATH=$(VENV_DIR)/bin:$(PATH) $(VENV_DIR)/bin/pip install -r requirements.txt

clean:
	rm -rf venv *.egg-info
