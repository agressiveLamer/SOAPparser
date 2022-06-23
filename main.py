import mimetypes

from bs4 import BeautifulSoup
from lxml.builder import unicode
import re

with open('f/2.xhtml') as f:
    soup = BeautifulSoup(f, 'lxml-xml')

for v in soup.find_all('element'):
    attrs = v.attrs  # присваиваем словарь с атрибутами тега
    for key in attrs:
        value = attrs[key]  # значение атрибута
        if key == 'name':
            name = value
            print(f'{key} = {name}')
        elif key == 'minOccurs':
            minOccurs = value
            print(f'{key} = {minOccurs}')
        elif key == 'maxOccurs':
            maxOccurs = value
            print(f'{key} = {maxOccurs}')
        elif key == 'id':
            elementID = value
            print(f'{key} = {elementID}')
        elif key == 'type':
            elementType = value
            print(f'{key} = {elementType}')
