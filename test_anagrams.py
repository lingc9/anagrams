from find_anagrams import make_anagrams_dict

list_1 = ["iceman", "cinema", "deposit", "aloof"]
list_2 = ["iceman", "cinema", "deposit", "cat", "bat", "act"]

print(make_anagrams_dict(list_1))


def test_small():
    list_1_dict = make_anagrams_dict(list_1)
    assert list_1_dict[''.join(sorted(list_1[0]))] == {'iceman', 'cinema'}
    assert list_1_dict[''.join(sorted(list_1[2]))] == {'deposit'}
    assert list_1_dict[''.join(sorted(list_1[3]))] == {'aloof'}
