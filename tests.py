from processing_text import TextFormating
from featching_manager import FeatchingData


def test_remove_punctation():
    text = 'New ?! example'
    got = TextFormating(text).remove_special_chars()
    expected = 'New    example'
    assert got == expected


def test_remove_special_chars():
    text = 'New\texample\n'
    got = TextFormating(text).remove_tabs_and_enters()
    expected = 'New example '
    assert got == expected
