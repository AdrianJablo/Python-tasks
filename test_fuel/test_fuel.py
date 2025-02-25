from fuel import convert, gauge
import pytest

def main():
    test_convert_gauge()
    test_zero_division()
    test_value()

def test_convert_gauge():
     assert convert("1/4") == 25 and gauge(25) == "25%"
     assert convert("1/100") == 1 and gauge(1) == "E"
     assert convert("99/100") == 99 and gauge(99) == "F"

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
         convert("1/0")
         
def test_value():
     with pytest.raises(ValueError):
        convert("cat/dog")

if __name__ == "__main__":
    main()
