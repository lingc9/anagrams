"""The driver code for find_anagrams.py, including input / output handling."""

from find_anagrams import make_anagrams_dict
import sys


def convert_to_list(file_path):
    word_list = [file_path]
    return word_list


def output(word_list):
    anagrams_dict = make_anagrams_dict(word_list)
    for key in anagrams_dict.keys():
        print(anagrams_dict[key])


list_1 = input("./" + str(sys.argv[1]))
print(output(list_1))
