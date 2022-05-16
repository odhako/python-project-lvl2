install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run gendiff

test:
	poetry install
	poetry build
	pip3 uninstall gendiff -y
	python3 -m pip install --user dist/*.whl
