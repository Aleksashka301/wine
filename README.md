# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Запуск

- Скачайте код
```python
git clone https://github.com/Aleksashka301/wine
```
- Установите виртуальное окружение
```python
python -m venv venv
```
- Активируйте виртуальное окружение
```python
venv\Scripts\Activate
```
- Установите необходимые библиотеки
```python
pip install -r requirements.txt
```
- Во время запуска скрипта необходимо указать два необязательных аргумента. Полный путь до файла, по умолчанию
стоит значение `wine3.xlsx`. Второй аргумент, лист файла, по умолчанию стоит `Лист1`. Запустите сайт командой
```python
python main.py
```
- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
