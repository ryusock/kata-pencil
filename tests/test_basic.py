import pytest
import sys
sys.path.append('../src')

from stationary import Pencil, Paper

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
