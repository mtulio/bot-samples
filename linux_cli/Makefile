
bot_user = bot_user
venv_name = .venv/

.PHONY: setup
setup:
	git submodule update --init --recursive

venv_activate:
	if [ -d ./.venv/ ]; then
		source ./.venv/bin/active
	else

.PHONY: dependencies
dependencies: venv_active
	apt-get install -y python-pip
	pip install -r requirements.txt


setup: venv active install
enable: venv_active
disable: venv_disable
install: python_req

venv:
	make venv

active:

deactive:
	venv disable

install:
	install re
