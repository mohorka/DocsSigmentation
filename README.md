# Documents' sigmentation
Программа, определяющая области интереса на документе

### Версия
Python 3.x

### Установка
1. `python3 -m venv env/.` - создание окружения (для windows:  `py -m venv env/.`)
2. `source env/bin/activate` - активация окружения (если падает с ошибкой, то меняем политику выполнения: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process` ,после снова шаг 2)
3. `pip install -r requirements.txt` - установка зависимостей

Таким образом, запуск одной командой: `python3 -m venv env/. && source env/bin/activate && pip install -r requirements.txt`
(Для Windows: `py -m venv env/. && source env/bin/activate && pip install -r requirements.txt`).

Для сохранения новых зависимостей в процессе работы : `pip freeze -l > requirements.txt`

### Пример результата работы
![Result](/result.jpg)
