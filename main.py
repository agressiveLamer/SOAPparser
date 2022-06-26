import mimetypes

from bs4 import BeautifulSoup
import csv
from lxml.builder import unicode
import re

with open('f/2.xhtml') as f:
    soup = BeautifulSoup(f, 'lxml-xml')

with open('f/result.csv', 'w') as result:
    writer = csv.writer(result)
    writer.writerow(
        ['name', 'type', 'minOccurs', 'maxOccurs', 'id']
    )

for v in soup.find_all('element'):
    attrs = v.attrs  # присваиваем словарь с атрибутами и значениями тега
    if attrs.get('maxOccurs') is None:
        with open('f/result.csv', 'a') as result:
            writer = csv.writer(result)
            writer.writerow(
                [attrs.get('name'),
                 attrs.get('type'),
                 attrs.get('minOccurs'),
                 '1',
                 attrs.get('id')]
            )
    elif attrs.get('minOccurs') is None:
        with open('f/result.csv', 'a') as result:
            writer = csv.writer(result)
            writer.writerow(
                [attrs.get('name'),
                 attrs.get('type'),
                 '1',
                 attrs.get('maxOccurs'),
                 attrs.get('id')]
            )
    else:
        with open('f/result.csv', 'a') as result:
            writer = csv.writer(result)
            writer.writerow(
                [attrs.get('name'),
                 attrs.get('type'),
                 attrs.get('minOccurs'),
                 attrs.get('maxOccurs'),
                 attrs.get('id')]
            )
