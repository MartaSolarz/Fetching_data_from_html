from M05_project import text_formating
from M05_project import extract


def test_remove_punctation():

    """Removing punctuation marks from text"""

    text = 'New ?! example'
    got = text_formating(text)
    expected = 'New    example'
    assert got == expected


def test_remove_special_chars():
    text = 'New\texample\n'
    got = text_formating(text)
    expected = 'New example '
    assert got == expected


def test_remove_whitespaces():

    """Removing whitespace at the beginning and end of a string"""

    text = '<b> Example </b>'
    xpath = '//b'
    got = extract(text, xpath)
    expected = ['Example']
    assert got == expected


def test_scrapper_reallife_website():
    with open('M05\Materiały Budowlane - Znajdź Materiały Budowlane w Leroy Merlin.html', encoding='utf8') as stream:
        content = stream.read()
    
    xpath = "//*[@id='product-categories']/div[1]/div[1]/ul/li/a"
    got = extract(content, xpath)
    expected = ['Cegły klinkierowe', 'Cegły  pustaki i bloczki betonowe', 'Cementy i Wapna', 'Piasek  keramzyt']
    assert got == expected
