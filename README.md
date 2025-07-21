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
mkdir -p lib_tmp_rep
touch lib_tmp_rep/__init__.py
uv pip install -e .
python -m build --wheel
uv pip install ./dist/lib_tmp_rep-0.1.0-py3-none-any.whl
mkdir -p /workspaces/lib-tmp-rep/lib_tmp_rep
cd /workspaces/project-tmp-rep
uv pip install -e ../lib-tmp-rep
```
 # Создайте обязательные файлы
```
cat > pyproject.toml <<EOL
[project]
name = "lib-tmp-rep"
version = "0.1.0"
```
```
[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"
EOL
```
# __init__.py
```
touch lib_tmp_rep/__init__.py
```

# Обновите func_lib
```
cat > lib_tmp_rep/func_lib.py <<EOL
def func_from_lib():
    return 42  # Пример реализации
EOL
```
# Установите пакет
```
uv pip install -e .
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
