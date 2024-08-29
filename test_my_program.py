import pytest
from myfile import error_prog

def test_passing_case():
    print(error_prog(str(10)))
    
def test_failing_case():
    print(error_prog(10))
    # This test should fail as it will raise a TypeError when trying to concatenate int to str directly
    # with pytest.raises(TypeError):
    #     print (error_prog(10))
