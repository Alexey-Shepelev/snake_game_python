install:
	poetry install

snake:
	poetry run python snake_game_python/snake_game.py

build:
	poetry build

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl

lint:
	poetry run flake8 brain_games

.PHONY: install build publish