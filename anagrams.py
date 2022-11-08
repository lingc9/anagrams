"""The driver code for find_anagrams.py, including input / output handling."""

from find_anagrams import make_anagrams_dict
import sys


def convert_to_list(file_path):
    my_file = open(file_path, "r")
    data = my_file.read()
    word_list = data.split("\n")
    my_file.close()
    return word_list


def anagram_output(word_list):
    anagrams_dict = make_anagrams_dict(word_list)

    for anagram in anagrams_dict.values():
        print(anagram)


list_1 = convert_to_list("./" + str(sys.argv[1]))
anagram_output(list_1)
