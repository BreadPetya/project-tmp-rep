# project-tmp-rep
## Установка 
```
pip install uv
pip install build
```
# Использование UV
## Создание виртуального окружения
```
uv venv .venv
source .venv/bin/activate
```
# Установка lib-tmp-rep в project-tmp-rep
```
cd /workspaces/project-tmp-rep
uv pip install -e ../lib-tmp-rep
```
# Установка пакетов
```
uv pip install .
```
# Подключение lib-tmp-rep
## Установите пакет в режиме разработки
```
cd /workspaces/lib-tmp-rep
uv pip install -e .
uv pip list | grep lib-tmp-rep #проверка установки
```
# Запуск проекта
```
python main.py
```
