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

def test_edit_raises_exception_on_nonstring_argument(pencil, paper):
    with pytest.raises(TypeError):
        pencil.edit(100, paper, 3)

def test_edit_raises_exception_on_nonpaper_argument(pencil, paper):
    with pytest.raises(TypeError):
        pencil.edit("apple", 100, 3)

def test_edit_raises_index_out_of_bounds_exception(pencil, paper):
    with pytest.raises(IndexError):
        pencil.edit("apple", paper, 3)

def test_edit_basic(pencil, paper):
    pencil.write("An apple a day keeps the doctor away", paper)
    pencil.erase("apple", paper)
    pencil.edit("onion", paper, 3)
    assert paper.text == "An onion a day keeps the doctor away"

def test_edit_collision(pencil, paper):
    pencil.write("An apple a day keeps the doctor away", paper)
    pencil.erase("apple", paper)
    pencil.edit("artichoke", paper, 3)
    assert paper.text == "An artich@k@ay keeps the doctor away"

def test_edit_collision_out_of_bounds(pencil, paper):
    """Although there is not enough space to write "artichoke"
    on the paper, EDIT will attempt the writeover until the end
    of the text, and then give up.
    """
    pencil.write("An apple", paper)
    pencil.erase("apple", paper)
    pencil.edit("artichoke", paper, 2)
    assert paper.text == "Anartich"

def test_edit_with_point_degradation(paper):
    pencil = Pencil(12, 0)
    pencil.write("life is good", paper)
    pencil.erase("good", paper)
    pencil.edit("okay", paper, 8)
    assert paper.text == "life is ok  "

def test_edit_whitespace_collision(pencil, paper):
    pencil.write("Conditional\nby weather", paper)
    pencil.edit( "Conditioner\nfor sale\n", paper)
    assert paper.text == "Condition@@\n@@r@@a@@@r"

def test_edit_collision_and_point_degradation(paper):
    """Recall that an uppercase letter has write cost of 2. This pencil
    has enough durability to write "Top", leaving a durability of 1. That's
     enough to write '@' to replace 'T' butnot 'p'
     """
    pencil = Pencil(5, 0)
    pencil.write("Top", paper)
    pencil.edit("Bot", paper)
    assert paper.text == "@op"
