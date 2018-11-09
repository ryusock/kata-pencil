import pytest
import sys
sys.path.append('../src')

from stationary import Pencil, Paper

@pytest.fixture
def paper():
    '''Returns a blank sheet of Paper'''
    return Paper()

@pytest.fixture
def pencil():
    '''Returns a Pencil with default parameters'''
    return Pencil()

def test_write_raises_exception_on_nonstring_argument(pencil, paper):
    with pytest.raises(TypeError):
        pencil.write(100, paper)

def test_write_raises_exception_on_nonpaper_argument(pencil, paper):
    with pytest.raises(TypeError):
        pencil.write("apple", 100)

def test_write_initial(pencil, paper):
    pencil.write("She sells sea shells", paper)
    assert paper.text == "She sells sea shells"

def test_write_append(pencil, paper):
    pencil.write("She sells sea shells", paper)
    pencil.write(" down by the sea shore", paper)
    assert paper.text == "She sells sea shells down by the sea shore"

def test_write_point_degradation_no_caps(paper):
    pencil = Pencil(4, 0)
    pencil.write("sudoku", paper)
    assert paper.text == "sudo"

def test_write_point_degradation_caps(paper):
    pencil = Pencil(4, 0)
    pencil.write("Sudoku", paper)
    assert paper.text == "Sud"

def test_write_point_degradation_at_cap(paper):
    pencil = Pencil(4, 0)
    pencil.write("sudO", paper)
    assert paper.text == "sud"

def test_write_point_degradation_with_blanks(paper):
    pencil = Pencil(10, 0)
    pencil.write("sudoku\n\n   ch a\nll\nenge", paper)
    assert paper.text == "sudoku\n\n   ch a\nl"
