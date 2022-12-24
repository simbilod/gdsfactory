help:
	@echo 'make install:          Install package, hook, notebooks and gdslib'
	@echo 'make test:             Run tests with pytest'
	@echo 'make test-force:       Rebuilds regression test'

full: gdslib plugins
	pip install -e .[docs,dev,full,gmsh,tidy3d,devsim,meow,sax]

install: gdslib
	pip install -e .[dev,full]
	pre-commit install
	gf tool install

dev: full
	pre-commit install
	gf tool install

mamba:
	bash mamba.sh

patch:
	bumpversion patch
	python docs/write_components_doc.py

minor:
	bumpversion minor
	python docs/write_components_doc.py

major:
	bumpversion major
	python docs/write_components_doc.py

plugins:
	mamba install pymeep=*=mpi_mpich_* -y
	mamba install slepc4py=*=complex* -y
	pip install -e .[tidy3d]
	pip install jax jaxlib
	pip install --upgrade "protobuf<=3.20.1"
	pip install femwell
	pip install scikit-fem[all] --upgrade

plugins-debian: plugins
	sudo apt-get install -y python3-gmsh

thermal:
	mamba install python-gmsh

gmsh:
	pip install trimesh mapbox_earcut gmsh meshio pygmsh pyvista h5py

meep:
	mamba install pymeep=*=mpi_mpich_* -y

sax:
	pip install jax jaxlib

publish:
	anaconda upload environment.yml

update-pre:
	pre-commit autoupdate --bleeding-edge

gds:
	python gdsfactory/components/straight.py

gdslib:
	git clone https://github.com/gdsfactory/gdslib.git -b data

test:
	flake8 gdsfactory
	pytest -s

test-force:
	echo 'Regenerating component metadata for regression test. Make sure there are not any unwanted regressions because this will overwrite them'
	rm -rf gdslib/gds/gds_ref
	rm -rf gdsfactory/samples/pdk/test_fab_c.gds
	pytest --force-regen

test-meep:
	pytest gdsfactory/simulation/gmeep

test-tidy3d:
	pytest gdsfactory/simulation/gtidy3d

test-gmsh:
	pytest gdsfactory/simulation/gmsh

test-femwell:
	pytest gdsfactory/simulation/fem

test-plugins:
	pytest gdsfactory/simulation/gmeep gdsfactory/simulation/modes gdsfactory/simulation/lumerical gdsfactory/simulation/gtidy3d gdsfactory/simulation/gmsh gdsfactory/tests/test_klayout
	pip list > requirements.txt

test-notebooks:
	py.test --nbval notebooks

diff:
	python gdsfactory/merge_cells.py

cov:
	pytest --cov=gdsfactory

venv:
	python3 -m venv env

pipenv:
	pip install pipenv --user
	pipenv install

pyenv3:
	pyenv shell 3.7.2
	virtualenv venv
	source venv/bin/activate
	python -V # Print out python version for debugging
	which python # Print out which python for debugging
	python setup.py develop

docker-debug:
	docker run -it joamatab/gdsfactory sh

docker-build:
	docker build -t joamatab/gdsfactory .

docker-run:
	docker run \
		-p 8888:8888 \
		-p 8082:8082 \
		-e JUPYTER_ENABLE_LAB=yes \
		joamatab/gdsfactory:latest

conda:
	conda env create -f environment.yml
	echo 'conda env installed, run `conda activate gdsfactory` to activate it'

mypy:
	mypy gdsfactory --ignore-missing-imports

build:
	rm -rf dist
	pip install build
	python -m build

upload-devpi:
	pip install devpi-client wheel
	devpi upload --format=bdist_wheel,sdist.tgz

upload-twine: build
	pip install twine
	twine upload dist/*

release:
	git push
	git push origin --tags

lint:
	tox -e flake8

pylint:
	pylint --rcfile .pylintrc gdsfactory/

lintdocs:
	flake8 --select RST

pydocstyle:
	pydocstyle gdsfactory

doc8:
	doc8 docs/

autopep8:
	autopep8 --in-place --aggressive --aggressive **/*.py

codestyle:
	pycodestyle --max-line-length=88

doc:
	python docs/write_components_doc.py

git-rm-merged:
	git branch -D `git branch --merged | grep -v \* | xargs`

link:
	lygadgets_link gdsfactory/klayout

constructor:
	mamba install constructor conda-libmamba-solver -y
	constructor .

.PHONY: gdsdiff build conda
