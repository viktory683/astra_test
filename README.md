# astra_test

## Содержание
- [astra\_test](#astra_test)
  - [Содержание](#содержание)
  - [Требования](#требования)
  - [Установка](#установка)
  - [Запуск](#запуск)
  - [TODO](#todo)


## Требования

- Qt4
- Python 3.6.15
- PySide2

## Установка

0. ```bash
   git clone https://github.com/viktory683/astra_test.git
   cd astra_test
   ```
   1. (опционально) Создать виртуальное окружение
      ```bash
      python3 -m venv .venv
      source .venv/bin/activate
      ```
1. Установить необходимые зависимости
   ```bash
   pip3 install -r requirements.txt
   ```

## Запуск
В случае использования виртуального окружения
```bash
/path/to/venv/bin/python3 /path/to/prroject/directory/widget.py
```

При установке зависимостей в глобальном окружении
```bash
python3 /path/to/project/directory/widget.py
```

## TODO

- [ ] Переработать фильтрацию для исправление бага со сбросом корня дерева на фильтре, с которым нет соответствий, фильтре вида `"/"`
- [ ] Протестировать установку с `Astra Linux Common Edition 2.12.46`