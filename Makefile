install:
	uv sync

brain-games:
	uv run brain-games

build: #Сборка пакета 
	uv build

package-install: #Установка пакета 
	uv tool install dist/*.whl


