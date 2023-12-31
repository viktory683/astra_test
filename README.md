# astra_test

![UI фото](previews/image.png)
![UI расширенный](previews/image-3.png)
![UI фото скрытые](previews/image-1.png)
![UI фото скрытые фильтр](previews/image-2.png)

## Содержание
- [astra\_test](#astra_test)
  - [Содержание](#содержание)
  - [Требования](#требования)
  - [Установка](#установка)
  - [Запуск](#запуск)
  - [TODO](#todo)
  - [Проблемы](#проблемы)
    - [Не удалось загрузить плагин платформы Qt "xcb" в "", хотя он был найден.](#не-удалось-загрузить-плагин-платформы-qt-xcb-в--хотя-он-был-найден)
      - [Решение](#решение)
        - [Обновить ссылку](#обновить-ссылку)
    - [Python `3.11.5`](#python-3115)
    - [PySide2 `5.13.2`](#pyside2-5132)
      - [Не работает](#не-работает)
      - [Ошибки](#ошибки)
      - [Решение](#решение-1)


## Требования

- Qt4
- Python 3.5.3
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
/path/to/venv/bin/python3 /path/to/project/directory/widget.py
```

При установке зависимостей в глобальном окружении
```bash
python3 /path/to/project/directory/widget.py
```

## TODO

- [ ] Протестировать с другими версиями PySide и Python
- [ ] Переработать фильтрацию для исправление бага со сбросом корня дерева на фильтре, с которым нет соответствий, фильтре вида `"/"`
- [ ] Выровнять все колонны, кроме имени по правому краю

## Проблемы

### Не удалось загрузить плагин платформы Qt "xcb" в "", хотя он был найден.
оригинал: `Could not load the Qt platform plugin "xcb" in "" even though it was found.`

#### Решение

1. Скачать последнюю версию `libxcb-util1` (ссылка на скачивание действительна на текущий момент `22/09/2023`.
   
   В случае возникновения ошибки `404 Not Found` необходимо заменить её на актуальную ([См. ниже](#обновить-ссылку)))
   ```bash
   wget -O libxcb-util1.deb http://ftp.de.debian.org/debian/pool/main/x/xcb-util/libxcb-util1_0.4.0-1+b1_amd64.deb
   ```
2. Установить пакет
   ```bash
   sudo dpkg -i libxcb-util1.deb
   ```

##### Обновить ссылку

Поиск по запросу `libxcb-util1` на [сайте](https://debian.pkgs.org/12/debian-main-amd64)

Выбрать необходимый репозиторий и архитектуру (`Debian 11 > amd64` сработал)

Секция `Download > Binary Package`

### Python `3.11.5`
### PySide2 `5.13.2`

#### Не работает
- Скрытые файлы (отключается фильтр и всегда видно всё)
- Поиск по строке (сброс дерева до корня)

#### Ошибки

```python
AttributeError: 'Widget' object has no attribute '_Widget__current_root'. Did you mean: '_Widget__new_root'?
```

#### Решение

[TODO](#todo)
