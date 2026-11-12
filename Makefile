install:
	uv sync

brain-games:
	uv run brain-games

build1: build package-install

build: #Сборка пакета 
	uv build

reinstall: #Переустановка новую версию пакета в операционную систему
	uv tool install --force dist/hexlet_code-0.1.0-py3-none-any.whl

package-install: #Установка пакета 
	uv tool install dist/*.whl

lint: #Проверка кода на соответствие стандартам 
	uv run ruff check brain_games
