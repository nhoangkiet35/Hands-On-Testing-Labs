from object.reverse_string import reverse_string

def test_empty_string():
    assert reverse_string("") == ""

def test_single_character_string():
    assert reverse_string("a") == "a"
    assert reverse_string("1") == "1"
    assert reverse_string("!") == "!"
    assert reverse_string("@") == "@"

def test_multiple_character_string():
    assert reverse_string("abc") == "cba"
    assert reverse_string("123") == "321"
    assert reverse_string("!@#") == "#@!"
    assert reverse_string("@#$") == "$#@"
    assert reverse_string("hello") == "olleh"

def test_string_with_spaces():
    assert reverse_string("hello world") == "dlrow olleh"
    assert reverse_string("123 456") == "654 321"
    assert reverse_string("!@# 456") == "654 #@!"
    assert reverse_string("@#$ 456") == "654 $#@"
    assert reverse_string("   hello world 123   ") == "   321 dlrow olleh   "