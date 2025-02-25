import pytest
from my_code import add_numbers  # ✅ Correct import

def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0

if __name__ == "__main__":
    pytest.main()
