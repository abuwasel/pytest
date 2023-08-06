import pytest

#------------------Fixtures----------------------------------#

@pytest.fixture
def my_fruite():
    return 'banana'

def test_fruite(my_fruite):
    assert my_fruite == 'banana'

#-------------------------------------------------------------

#------------------Fixtures with list------------------------#
@pytest.fixture
def order():
    return []

@pytest.fixture
def append_first(order):
    order.append(1)

@pytest.fixture
def append_second(order, append_first):
    order.extend([2,3,4])

@pytest.fixture(autouse=True)
def append_third(order, append_second):
    order += [5]

def test_order(order):
    assert order == [1, 2, 3, 4, 5]