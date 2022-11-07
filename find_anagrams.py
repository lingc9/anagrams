"""Functions used to take a list of words and returns a suitable data structure
with the words grouped into anagram sets"""


def match_dict_key(word, keys):
    """When given a word find the key that is the same anagram. Return None
    otherwise.

    Parameters:
        word (str): A word as a string.
        keys (dict): Dictionary keys.

    Returns:
        key (str): Dictionary key that is an anagram of word.
    """
    for key in keys:
        if sorted(word) == sorted(key):
            return key

    return None


def make_anagrams_dict(words):
    """When given a list of strings, return a dictionary of anagrams.

    Parameters:
        words (list): A list of words.

    Returns:
        anagrams_dict (dict): A dictionary of keys that are words and values
        that are all anagrams from the list.
    """
    anagrams_dict = {}

    for word in words:
        word = word.lower()
        word_dict_key = match_dict_key(word, anagrams_dict.keys())

        if word_dict_key:
            anagrams_dict[word_dict_key].append(word)
        else:
            anagrams_dict[word] = [word]

    return anagrams_dict
