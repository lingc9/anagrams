from find_anagrams import make_anagrams_dict

list_1 = ["iceman", "cinema", "deposit", "aloof"]
list_2 = ["iceman", "cinema", "deposit", "cat", "bat", "act"]
list_3 = ["aloof", "aloof", "aloof", "aloof"]
list_4 = ["iCemAn", "cINeMa"]
list_5 = ["ICEMAN", "cinema"]
list_6 = ["a", "A"]
list_7 = []


def test_lists():
    list_1_dict = make_anagrams_dict(list_1)
    assert list_1_dict[''.join(sorted(list_1[0]))] == {'iceman', 'cinema'}
    assert list_1_dict[''.join(sorted(list_1[2]))] == {'deposit'}
    assert list_1_dict[''.join(sorted(list_1[3]))] == {'aloof'}

    list_2_dict = make_anagrams_dict(list_2)
    assert list_2_dict[''.join(sorted(list_2[0]))] == {'iceman', 'cinema'}
    assert list_2_dict[''.join(sorted(list_2[2]))] == {'deposit'}
    assert list_2_dict[''.join(sorted(list_2[3]))] == {'act', 'cat'}
    assert list_2_dict[''.join(sorted(list_2[4]))] == {'bat'}

    list_3_dict = make_anagrams_dict(list_3)
    assert list_3_dict[''.join(sorted(list_3[0]))] == {'aloof'}


def test_empty():
    assert make_anagrams_dict(list_7) == {}


def test_capitalization():
    list_4_dict = make_anagrams_dict(list_4)
    lower_4 = list_4[0].lower()
    assert list_4_dict[''.join(sorted(lower_4))] == {'iceman', 'cinema'}

    list_5_dict = make_anagrams_dict(list_5)
    lower_5 = list_5[0].lower()
    assert list_5_dict[''.join(sorted(lower_5))] == {'iceman', 'cinema'}

    list_6_dict = make_anagrams_dict(list_6)
    lower_6 = list_6[0].lower()
    assert list_6_dict[''.join(sorted(lower_6))] == {'a'}
