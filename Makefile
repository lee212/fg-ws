######################################################################
# INSTALLATION
######################################################################
dist:
	make -f Makefile pip

pip:
	make -f Makefile clean
	python setup.py sdist

force:
	make -f Makefile pip
	sudo pip install -U dist/*.tar.gz

install:
	sudo pip install dist/*.tar.gz

######################################################################
# PYPI
######################################################################

upload:
	make -f Makefile pip
#	python setup.py register
	python setup.py sdist upload

######################################################################
# QC
######################################################################

qc-install:
	sudo pip install pep8
	sudo pip install pylint
	sudo pip install pyflakes

qc:
	pep8 ./futuregrid/virtual/cluster/
	pylint ./futuregrid/virtual/cluster/ | less
	pyflakes ./futuregrid/virtual/cluster/

# #####################################################################
# CLEAN
# #####################################################################


clean:
	find . -name "*~" -exec rm {} \;  
	find . -name "*.pyc" -exec rm {} \;  
	rm -rf build dist *.egg-info *~ #*

######################################################################
# pypi
######################################################################

pip-register:
	python setup.py register

upload:
	make -f Makefile pip
	python setup.py sdist upload

#############################################################################
# PUBLISH GIT HUB PAGES
#############################################################################

gh-pages:
	git checkout gh-pages
	make
