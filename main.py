import mimetypes

from bs4 import BeautifulSoup
import csv
from lxml.builder import unicode
import re

with open('f/2.xhtml') as f:
    soup = BeautifulSoup(f, 'lxml-xml')


def parser(XMLfile):
    keys = []
    for v in soup.find_all('element'):
        attrs = v.attrs  # присваиваем словарь с атрибутами и значениями тега
        for key in attrs:
            value = attrs[key]  # значение атрибутов
            keys = keys.append(key) #не работает..
            with open('f/result.csv', mode='a') as result:
                writer = csv.writer(result)
                writer.writerow(
                    (key)
                )
            """if key == 'name':
                name = value
            elif key == 'minOccurs':
                minOccurs = value
            elif key == 'maxOccurs':
                maxOccurs = value
            elif key == 'id':
                elementID = value
            elif key == 'type':
                elementType = value
            """


print(parser(soup))
