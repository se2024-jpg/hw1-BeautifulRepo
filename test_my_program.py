import pytest
from myfile import error_prog

def test_passing_case():
    # This test should pass because the integer is converted to a string explicitly
    assert error_prog(str(10)) == "10HelloWorld!"

def test_failing_case():
    # This test should fail as it will raise a TypeError when trying to concatenate int to str directly
    with pytest.raises(TypeError):
        error_prog(10)
