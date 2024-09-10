import pytest
import sys
import os

# Add the ../src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from myfile import error_prog

def test_passing_case():
    # This will pass as var1 is converted to string
    result = error_prog(str(10))
    print(result)  # Print the result

def test_failing_case():
    # This will fail due to type error when concatenating an int with strings
    with pytest.raises(TypeError):  # Expecting a TypeError
        error_prog(10)
