import pytest

import sys, os
import pytest
sys.path.append(os.path.join(sys.path[0],'src'))
from demo import simple_function

def test_answer():
    assert 3 == 3


def test_simple_function():
    assert simple_function(1) == 2


variable_names = "input,expected"
values = [(1, 2),
          (3, 4), 
          (6, 7)]

@pytest.mark.parametrize(variable_names, values)
def test_parameterized(input,expected):
    assert simple_function(input) == expected
