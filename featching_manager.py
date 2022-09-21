from lxml.html import fromstring

import requests

from processing_text import TextFormating


class FeatchingData:
    def __init__(self, page_adress, xpath) -> None:
        self.adress = requests.get(page_adress)
        self.text = None
        self.xpath = xpath
        self.elements = None

    def is_valid(self) -> bool:
        if self.adress.ok:
            return True
        else:
            print('URL error.')
            return False

    def run(self):
        if self.is_valid():
            self.text = self.adress.text
            elements = self.extract_elements()

            return elements
    
    def extract_elements(self):
        tree = fromstring(self.text)
        self.elements = tree.xpath(self.xpath)
        return self.process()

    def process(self):
        return [TextFormating(el.text_content()).process() for el in self.elements]
