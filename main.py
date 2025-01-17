from jinja2 import Environment, FileSystemLoader, select_autoescape
from http.server import HTTPServer, SimpleHTTPRequestHandler
from collections import defaultdict
import argparse
import datetime
import pandas
import os


YEAR_WINERY_FOUNDATION = 1920


def getting_age_winery(age):
    if str(age)[-2:] in ['11', '12', '13', '14'] or str(age)[-1] in '056789':
        return 'лет'
    elif str(age)[-1] in '1':
        return 'год'
    else:
        return 'года'


def getting_information_drinks(file, sheet):
    wine_information = pandas.read_excel(file, sheet_name=sheet)
    wine_information = wine_information.fillna('')
    wine_information = wine_information.values.tolist()

    information_drinks = defaultdict(list)
    for drink in wine_information:
        image = drink[4]
        image_path = os.path.join('images/', image)

        if not os.path.exists(image_path):
            image = 'image.png'

        information_drinks[drink[0]].append({
            'Картинка': image,
            'Категория': drink[0],
            'Название': drink[1],
            'Сорт': drink[2],
            'Цена': drink[3],
            'Акция': drink[5]
        })

    information_drinks = dict(information_drinks)
    return dict(sorted(information_drinks.items()))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path_and_name_file', nargs='?', default='wine3.xlsx', type=str)
    parser.add_argument('sheet', nargs='?', default='Лист1', type=str)
    args = parser.parse_args()
    drinks_file = args.path_and_name_file
    sheet_file = args.sheet
    age_winery = datetime.datetime.now().year - YEAR_WINERY_FOUNDATION

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')

    try:
        rendered_page = template.render(
            age_winery=age_winery,
            year=getting_age_winery(age_winery),
            information_drinks=getting_information_drinks(drinks_file, sheet_file)
        )

        with open('index.html', 'w', encoding="utf8") as file:
            file.write(rendered_page)

        server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
        server.serve_forever()
    except FileNotFoundError:
        print('Файл не найден')


