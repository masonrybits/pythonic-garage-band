from band import Band, Musician, Guitarist, Bassist, Drummer

import pytest

def test_instrument_guitarist():
    g = Guitarist('Ting')
    expected = 'guitar'
    actual = g.get_instrument()
    assert actual == expected

def test_instrument_bassist():
    g = Bassist('Ting')
    expected = 'bass'
    actual = g.get_instrument()
    assert actual == expected

def test_instrument_drummer():
    g = Drummer('Ting')
    expected = 'drum'
    actual = g.get_instrument()
    assert actual == expected

def test_solo_guitar():
    g = Guitarist('Ting')
    expected = 'Ting plays guitar solo. '
    actual = g.play_solo()
    assert actual == expected

def test_solo_bass():
    g = Guitarist('Ting')
    expected = 'Ting plays guitar solo. '
    actual = g.play_solo()
    assert actual == expected

def test_solo_drum():
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
    assert actual == expected

def test_create_from_data_str():
    data = """FunBand
Ting on Guitar
Tang on Bass
Teng on Drum"""
    b = Band.create_from_data(data)
    expected = 'The band is named FunBand, the members are Ting Tang Teng '
    actual = b.__str__()
    assert actual == expected

def test_create_from_data_repr():
    data = """FunBand
Ting on Guitar
Tang on Bass
Teng on Drum"""
    b = Band.create_from_data(data)
    expected = 'FunBand - [Ting - guitar - guitar solo, Tang - bass - bass solo, Teng - drum - drum solo]'
    actual = b.__repr__()
    assert actual == expected

@pytest.fixture(autouse=True)
def clean():
    Band.all = []
