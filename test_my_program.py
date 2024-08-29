import pytest
from myfile import error_prog

def test_passing_case():
    print(error_prog(str(10)))
    
def test_failing_case():
    print(error_prog(10))
