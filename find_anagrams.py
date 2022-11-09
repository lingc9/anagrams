"""Functions used to take a list of words and returns a suitable data structure
with the words grouped into anagram sets"""


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
        key = ''.join(sorted(word))

        if key in anagrams_dict:
            anagrams_dict[key].add(word)
        else:
            anagrams_dict[key] = {word}

    return anagrams_dict
