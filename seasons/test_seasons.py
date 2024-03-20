from seasons import check_birth_date

def test_check_birthday():
    assert check_birth_date("2000-01-27") == ("2000", "01", "27")
    assert check_birth_date("2000-1-2") == None
    assert check_birth_date("July 3, 1998") == None
