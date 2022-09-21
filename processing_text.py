from typing import NoReturn
from string import punctuation


class TextFormating:
    def __init__(self, content: str) -> NoReturn:
        self.content = content
        self.new_content = ''

    def remove_tabs_and_enters(self):
        return self.content.replace('\n', ' ').replace('\t', ' ')

    def remove_special_chars(self):
        for char in self.content:
            if char in punctuation:
                self.new_content += char.replace(char, ' ')
            else:
                self.new_content += char
        
        return self.new_content

    def remove_rsplit_and_lsplit(self):
        self.new_content = self.new_content.rstrip().lstrip()

        return self.new_content

    def process(self):
        self.content = self.remove_tabs_and_enters()
        self.remove_special_chars()
        self.remove_rsplit_and_lsplit()

        return self.new_content
