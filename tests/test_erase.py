import pytest
import sys
sys.path.append('../src')

from stationary import Pencil, Paper

@pytest.fixture
def paper():
    '''Returns a black sheet of Paper'''
    return Paper()

@pytest.fixture
def pencil():
    '''Returns a Pencil with default parameters'''
    return Pencil()

def test_erase_raises_exception_on_nonstring_argument(pencil, paper):
    with pytest.raises(TypeError):
        pencil.erase(100, paper)

def test_erase_basic(pencil, paper):
    pencil.write("Bonjour madame", paper)
    pencil.erase("madame", paper)
    assert paper.text == "Bonjour       "

def test_erase_last_occurence_of_text(pencil, paper):
    pencil.write("time and time again", paper)
    pencil.erase("time", paper)
    assert paper.text == "time and      again"

def test_erase_text_not_found(pencil, paper):
    pencil.write("Claire de lune", paper)
    pencil.erase("moon", paper)
    assert paper.text == "Claire de lune"

def test_erase_multiple_times(pencil, paper):
    pencil.write("How much wood would a woodchuck chuck if a woodchuck could chuck wood?", paper)
    pencil.erase("chuck", paper)
    pencil.erase("chuck", paper)
    pencil.erase("chuck", paper)
    pencil.erase("chuck", paper)
    assert paper.text == "How much wood would a wood            if a wood      could       wood?"

def test_erase_degradation_basic(paper):
    pencil = Pencil(10, 5, 3)
    pencil.write("Buffalo Bill", paper)
    pencil.erase("Bill", paper)
    assert paper.text == "Buffalo B   "

def test_erase_degradation_with_whitespace(paper):
    pencil = Pencil(10, 5, 3)
    pencil.write("Y. M. C. A.", paper)
    pencil.erase("Y. M. C. A.", paper)
    assert paper.text == "Y. M. C    "

def test_erase_degradation_with_trailing_whitespace(paper):
    pencil = Pencil(10, 5, 4)
    pencil.write(" Time's\n up  ", paper)
    pencil.erase(" Time's\n up  ", paper)
    assert paper.text == " Time  \n     "
