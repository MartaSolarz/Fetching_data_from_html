"""PROJECT - MODULE 5 - REFACTOR - 20.09.2022"""

import click

from display_elements import DisplayInformation
from featching_manager import FeatchingData

@click.command()
@click.argument('page_adress')
@click.argument('xpath')    

def main(page_adress, xpath):
    formatting_elements = FeatchingData(page_adress, xpath).run()
    DisplayInformation(formatting_elements).run()
   

if __name__ == '__main__':
    main()
