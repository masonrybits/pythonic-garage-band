from band import Band, Musician, Guitarist, Bassist, Drummer

import pytest

def test_instrument():
    g = Guitarist('Ting')
    expected = 'guitar'
    actual = g.get_instrument()
    assert actual == expected

def test_solo():
    g = Guitarist('Ting')
    expected = 'Ting plays guitar solo. '
    actual = g.play_solo()
    assert actual == expected

def test_band_empty():
    b = Band('FunBand', [])
    expected = ''
    actual = b.play_solos()
    assert actual == expected

def test_band():
    b = Band('FunBand', [Guitarist('Ting'), Bassist('Tang')])
    expected = 'Ting plays guitar solo. Tang plays bass solo. '
    actual = b.play_solos()
    assert actual == expected

def test_list():
    b = Band('FunBand', [Guitarist('Ting'), Bassist('Tang')])
    expected = 'The band is named FunBand, the members are Ting Tang '
    actual = b.to_list()
    print(actual)
    assert actual == expected

@pytest.fixture(autouse=True)
def clean():
    Band.all = []
