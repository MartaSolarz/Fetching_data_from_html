### PROJECT - MODULE 5 - 5.06.2022

import click
from lxml.html import fromstring
import requests
import sys

def text_formating(content):

    """
    Removing special characters from the given text.
    
    parameters:
        text;
    return:
        new text without punctations.
    """

    SPECIAL_CHARS = '.,!?'
    content = content.replace('\n', ' ').replace('\t', ' ')

    new_content = ''
    for char in content:
        if char in SPECIAL_CHARS:
            new_content += char.replace(char, ' ')
        else:
            new_content += char

    return new_content
    
    
def extract(page_content, xpath):

    """ 
    Finding elements that match xpath in the html.

    parameters:
        html;
        xpath (foramt: " ... ")
    return:
        list of strings.
    """

    tree = fromstring(page_content)
    elements = tree.xpath(xpath)
    stripped = [text_formating(el.text_content()) for el in elements]
    elements_formating = [el.lstrip().rstrip() for el in stripped]

    return elements_formating


@click.command()
@click.argument('page_adress')
@click.argument('xpath')    

def main(page_adress, xpath):
    content = requests.get(page_adress)

    if not content.ok:
        print('URL error')
        sys.exit(1)
    
    text = content.text

    elements = extract(text, xpath)
    
    for el in elements:
        print('-', el)
    

if __name__ == '__main__':
    main()
