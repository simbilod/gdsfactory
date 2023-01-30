help:
	@echo 'make install:          Install package, hook, notebooks and gdslib'
	@echo 'make test:             Run tests with pytest'
	@echo 'make test-force:       Rebuilds regression test'

full: gdslib plugins
	pip install -e .[docs,dev,full,gmsh,tidy3d,devsim,meow,sax]

install:
	pip install -e .[full,dev] pre-commit
	pre-commit install
	gf tool install

dev: full
	pre-commit install
	gf tool install

mamba:
	bash conda/mamba.sh

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
	conda install -n base conda-libmamba-solver -y
	conda config --set solver libmamba
	conda install -c conda-forge pymeep=*=mpi_mpich_* nlopt -y
	conda install -c conda-forge slepc4py=*=complex* -y
	pip install jax jaxlib numpy femwell --upgrade
	pip install -e .[tidy3d,ray]

plugins-mamba:
	mamba install -c conda-forge pymeep=*=mpi_mpich_* nlopt -y
	mamba install -c conda-forge slepc4py=*=complex* -y
	pip install jax jaxlib numpy femwell --upgrade
	pip install -e .[tidy3d,ray,sax,devsim,meow]

plugins-debian: plugins
	sudo apt-get update
	sudo apt-get install -y python3-gmsh

thermal:
	conda install python-gmsh

gmsh:
	pip install trimesh mapbox_earcut gmsh meshio pygmsh pyvista h5py

meep:
	conda install pymeep=*=mpi_mpich_* -y

sax:
	pip install jax jaxlib

publish:
	anaconda upload environment.yml

update-pre:
	pre-commit autoupdate --bleeding-edge

gds:
	python gdsfactory/components/straight.py

gdslib:
	rm -rf $(HOME)/.gdsfactory
	git clone https://github.com/gdsfactory/gdslib.git -b main $(HOME)/.gdsfactory
gdslib-link:
	rm -rf $(HOME)/.gdsfactory
	ln -sf gdslib $(HOME)/.gdsfactory

test:
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
	pytest gdsfactory/simulation/gmeep gdsfactory/simulation/modes gdsfactory/simulation/lumerical gdsfactory/simulation/gtidy3d gdsfactory/simulation/gmsh gdsfactory/tests/test_klayout gdsfactory/simulation/fem

test-plugins-no-tidy3d:
	pytest gdsfactory/simulation/gmeep gdsfactory/simulation/modes gdsfactory/simulation/lumerical gdsfactory/simulation/gmsh gdsfactory/tests/test_klayout gdsfactory/simulation/fem

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
	conda install constructor -y
	constructor conda

nbqa:
	nbqa blacken-docs docs/notebooks/**/*.ipynb --nbqa-md
	nbqa blacken-docs docs/notebooks/*.ipynb --nbqa-md
	nbqa isort docs/notebooks/*.ipynb --float-to-top
	nbqa isort docs/notebooks/**/*.ipynb --float-to-top
	nbqa ruff --fix docs/notebooks/*.ipynb
	nbqa ruff --fix docs/**/*.ipynb
	nbqa autopep8 -i docs/notebooks/*.ipynb
	nbqa autopep8 -i docs/notebooks/**/*.ipynb

notebooks:
	nbstripout --drop-empty-cells docs/notebooks/*.ipynb


.PHONY: gdsdiff build conda gdslib
