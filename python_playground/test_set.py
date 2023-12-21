import pytest


@pytest.fixture
def setup():
   return set([1,1,2,3])
    
    
def test_set_size(setup):
    nums = setup
    
    assert len(nums) == 3

@pytest.mark.parametrize("expected,falseCase",[(1,5),(2,6),(3,7)])
def test_set_contains(setup,expected,falseCase):
    nums = setup
    
    assert expected in nums
    assert falseCase not in nums
