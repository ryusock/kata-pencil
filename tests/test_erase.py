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

def test_erase_nothing():
    return
