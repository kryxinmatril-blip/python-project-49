install:
	uv sync

brain-games:
	uv run brain-games

build1: build package-install

build: #Сборка пакета 
	uv build

package-install: #Установка пакета 
	uv tool install dist/*.whl

lint: #Проверка кода на соответствие стандартам 
	uv run ruff check brain_games
