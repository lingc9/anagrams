"""The driver code for find_anagrams.py, including input / output handling."""

from find_anagrams import make_anagrams_dict
import sys


def convert_to_list(file_path):
    """Takes a given file and converts the text in it into a list. Expects each
    word to have its own line."""
    my_file = open(file_path, "r")
    data = my_file.read()
    word_list = data.split("\n")
    my_file.close()
    return word_list


def anagram_output(word_list):
    """Runs the function to find anagrams on a list of words and outputs the
    results into a file named anagram_sets.txt, with each anagram printed on a
    new line."""
    anagrams_dict = make_anagrams_dict(word_list)
    file = open("anagram_sets.txt", "w")

    for anagram in anagrams_dict.values():
        file.write("'{}'\n".format(anagram))

    file.close()


list_1 = convert_to_list("./" + str(sys.argv[1]))
anagram_output(list_1)
