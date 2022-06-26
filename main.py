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

BaseListOfElements = []
for v in soup.find_all('element'):
    attrs = v.attrs  # присваиваем словарь с атрибутами и значениями тега
    with open('f/result.csv', 'a') as result:
        writer = csv.writer(result)
        writer.writerow(
            [attrs.get('name'),
             attrs.get('type'),
             attrs.get('minOccurs'),
             attrs.get('maxOccurs'),
             attrs.get('id')]
        )
