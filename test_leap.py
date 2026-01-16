from leap import is_leap

def test_is_leap():
    assert is_leap(2020) == True      # Leap year
    assert is_leap(1900) == False     # Not a leap year
    assert is_leap(2000) == True      # Leap year
