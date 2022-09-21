from typing import NoReturn


class DisplayInformation:
    def __init__(self, elements) -> NoReturn:
        self.elements = elements

    def print_element(self, el) -> NoReturn:
        print('-', el)
    
    def print_title(self) -> NoReturn:
        print()
        print('Items found:')
    
    def run(self) -> NoReturn:
        self.print_title()
        for el in self.elements:
            self.print_element(el)
        print()