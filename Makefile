ifndef VERBOSE
.SILENT:
endif

VERSION := '0.0.0'

.PHONY: test bootstrap

test: _virtualenv dependencies
	(source venv/bin/activate;								\
	coverage run --source=./mjb_test -m unittest discover -v tests/ && coverage report -m;	\
	deactivate)

rpm: test
	fpm -s dir --rpm-os linux -t rpm -n mjb-test -p ./RPMS/ -v $(VERSION) .

dependencies: _virtualenv
	(source venv/bin/activate;	\
	bundle install;			\
	pip install -r requirements.txt)

_virtualenv:
	virtualenv venv
	venv/bin/pip install -q --upgrade pip
	venv/bin/pip install -q --upgrade setuptools
