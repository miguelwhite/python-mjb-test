ifndef VERBOSE
.SILENT:
endif

PYTHON := $(shell which python)

.PHONY: test bootstrap

test:
	coverage run --source=./mjb_test -m unittest discover -v tests/ && coverage report -m

rpm:
	fpm -s dir --rpm-os linux -t rpm -n mjb-test -p ./RPMS/ .

_virtualenv:
	virtualenv venv
	venv/bin/pip install -q --upgrade pip
	venv/bin/pip install -q --upgrade setuptools
