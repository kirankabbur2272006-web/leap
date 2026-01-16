from leap import is_leap

def test_is_leap():
    assert is_leap(2020) is True

def test_not_leap():
    assert is_leap(1900) is False

def test_2000():
    assert is_leap(2000) is True
