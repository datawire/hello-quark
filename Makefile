SOURCES=1_hello_quark
VENV=etc/venv
PYTHON=$(VENV)/bin/python
QUARK_COMPILE=quark compile --python

all: clean compile hello

clean:
	rm -rf $(SOURCES)/hello etc/virtenv
	
compile: venv
	$(QUARK_COMPILE) $(SOURCES)/hello.q 
	
hello: compile
	$(PYTHON) $(SOURCES)/hello.py

vinstall: vinit
	( \
		source $(VENV)/bin/activate; \
		pip install -r requirements.txt; \
	)

vinit: clean
	virtualenv $(VENV)
	
vcompile: vinstall
	( \
		source $(VENV)/bin/activate; \
		$(QUARK_COMPILE) $(SOURCES)/hello.q -o $(SOURCES)/hello; \
	)
	
vhello: vcompile
	( \
		source $(VENV)/bin/activate; \
		python $(SOURCES)/hello.py; \
	)

vupdate: venv/bin/activate
	
venv/bin/activate: requirements.txt
	test -d $(VENV) || virtualenv $(VENV)
	$(VENV)/bin/pip install -Ur requirements.txt
	touch $(VENV)/bin/activate