import pytest
import sys
sys.path.append('../src')

from stationary import Pencil, Paper

def test_write_raises_exception_on_nonstring_argument():
    pencil = Pencil()
    paper = Paper()
    with pytest.raises(TypeError):
        pencil.write(100, paper)


def test_write_initial():
    pencil = Pencil()
    paper = Paper()
    pencil.write("She sells sea shells", paper)
    assert paper.text == "She sells sea shells"

def test_write_append():
    pencil = Pencil()
    paper = Paper()
    pencil.write("She sells sea shells", paper)
    pencil.write(" down by the sea shore", paper)
    assert paper.text == "She sells sea shells down by the sea shore"

def test_write_point_degradation_no_caps():
    pencil = Pencil(4, 0)
    paper = Paper()
    pencil.write("sudoku", paper)
    assert paper.text == "sudo"

def test_write_point_degradation_caps():
    pencil = Pencil(4, 0)
    paper = Paper()
    pencil.write("Sudoku", paper)
    assert paper.text == "Sud"

def test_write_point_degradation_at_cap():
    pencil = Pencil(4, 0)
    paper = Paper()
    pencil.write("sudO", paper)
    assert paper.text == "sud"

def test_write_point_degradation_with_blanks():
    pencil = Pencil(10, 0)
    paper = Paper()
    pencil.write("sudoku\n\n   ch a\nll\nenge", paper)
    assert paper.text == "sudoku\n\n   ch a\nl"
