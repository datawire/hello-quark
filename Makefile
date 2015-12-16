# Copyright 2015 Datawire. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

SOURCES=1_hello_quark
VENV=etc/venv
PYTHON=$(VENV)/bin/python

QUARK_OPTS=--python --python-out=.
QUARK_PACKAGE=quark package $(QUARK_OPTS)
QUARK_COMPILE=quark compile $(QUARK_OPTS)

all: clean vcompile

clean:
	rm -rf $(SOURCES)/hello etc/virtenv

vinit: clean
	virtualenv $(VENV)

vinstall: vinit
	( \
		source $(VENV)/bin/activate; \
		pip install -r requirements.txt; \
	)

vcompile: vinstall
	( \
		source $(VENV)/bin/activate; \
		$(QUARK_COMPILE) $(SOURCES)/hello.q -o $(SOURCES)/hello; \
		pip install $(SOURCES)/hello/dist/HelloQuark-1.0.0-py2-none-any.whl; \
	)

vpackage: vinstall
	( \
		source $(VENV)/bin/activate; \
		$(QUARK_PACKAGE) $(SOURCES)/hello.q -o $(SOURCES)/hello; \
		pip install $(SOURCES)/hello/dist/HelloQuark-1.0.0-py2-none-any.whl; \
	)

hello:
	( \
		source $(VENV)/bin/activate; \
		python $(SOURCES)/hello.py; \
	)

venv: venv/bin/activate

venv/bin/activate: requirements.txt
	test -d $(VENV) || virtualenv $(VENV)
	$(VENV)/bin/pip install -Ur requirements.txt
	touch $(VENV)/bin/activate