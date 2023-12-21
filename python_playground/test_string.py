import pytest

def test_replace():
    actual = "abc".replace("abc","adb")
    assert actual == "adb"
    
    
def test_split():
    seperator = ","
    actual =  "1,2".split(seperator)
    assert actual == ["1","2"]
    
    
def test_split_one_number():
    seperator = ","
    actual =  "1".split(seperator)
    assert actual == ["1"]
    
def test_delete_bracket():
    actual = "(1,2)"[1:4].split(',')
    assert actual == ["1","2"]
    
def test_charAt():
    actual = "abc"[0]
    assert actual == "a"
    

def test_charAt_raiseError():
    with pytest.raises(IndexError):
        actual = "abc"[55]
        assert actual == "a"