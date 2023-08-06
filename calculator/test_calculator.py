import pytest
import calculator


def test_multiplication():
   assert calculator.multiplication(4, 2) == 8


#You can add a (@pytest.mark) decorator above the functions and give them names to then run only the functions that have the desired property. This is what a decorator of this type looks like with the "int" attribute:
@pytest.mark.int
def test_add():
   assert calculator.add(2, 3) == 5

@pytest.mark.int
def test_subtract():
   assert calculator.subtract(5, 2) == 3


#----If we want to skip test for this function-------------------
@pytest.mark.skip(reason="No need right now!")
@pytest.mark.str
def test_add_strings():
   result = calculator.add("Hello", " unit test")
   assert result == "Hello unit test"
   assert type(result) is str
   assert "Hello" in result
   assert "world" not in result


#------------------Parametrize----------------------------------#
@pytest.mark.parametrize('num1, num2, res',[(8, 2, 10),(5, 9, 14),(6, 6, 12)])
def test_add_3(num1, num2, res):
    assert calculator.add(num1, num2) == res


@pytest.mark.parametrize('num1, num2, res',
    [
    (8, 2, 10),
    ("Hello", " unit test", "Hello unit test"),
    (round(8.0, 1), round(4.7, 1), round(12.7, 1))
    ])
def test_add_2(num1, num2, res):
    assert calculator.add(num1, num2) == res