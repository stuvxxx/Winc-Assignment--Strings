from enum import unique
from string import ascii_lowercase
from unittest import result
from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"


""" Write your functions here. """

# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`

if __name__ == "__main__":
    countries = get_countries()



def shortest_names(list): 
    result = []
    smallest_length = len((min(list, key = len)))
    for country in list: 
        if len(country) == smallest_length:
            result.append(country);
    return result


def most_vowels(list):
    first_place = int
    second_place = int
    third_place = int
    total_count_list = []
    result = []
    final_result = []
    def count_vowels_place_in_result(country, place): 
        vowel_counts = {}
        for vowel in "aeiou":
            count = country.lower().count(vowel)
            vowel_counts[vowel] = count
            counts = vowel_counts.values()
            total_vowels = sum(counts)
            if total_vowels == place:
                result.append(country)
    def count_vowels(country): 
        vowel_counts = {}
        for vowel in "aeiou":
            count = country.lower().count(vowel)
            vowel_counts[vowel] = count
            counts = vowel_counts.values()
            total_vowels = sum(counts)
            total_count_list.append(total_vowels)
    for country in list:
        count_vowels(country)
    first_place = (max(total_count_list))
    try:
        while True:
            total_count_list.remove(first_place)
    except ValueError:
        pass
    second_place = (max(total_count_list))
    try:
        while True:
            total_count_list.remove(second_place)
    except ValueError:
        pass
    third_place = (max(total_count_list))
    for country in list:
        count_vowels_place_in_result(country, first_place)
    for country in list:
        count_vowels_place_in_result(country, second_place)
    for country in list:
        count_vowels_place_in_result(country, third_place)
    for i in result:
        if i not in final_result:
            final_result.append(i)
    print(final_result)
    final_final_result = []
    final_final_result.append(final_final_result[0])
    final_final_result.append(final_final_result[1])
    final_final_result.append(final_final_result[2])
    print(final_final_result)



def alphabet_set(list):
    get_alphabet = ascii_lowercase
    letter_list = []
    for letter in get_alphabet:
        letter_list.append(letter)
    received_letter_list = []
    unique_letters_amount_list = []
    country_with_most_letters = ""
    letters_to_search_for = []
    final_list = []
    for country in list:
        unique_characters = set(country.lower())
        unique_letters_amount_list.append(len(unique_characters))
    most_letters = (max(unique_letters_amount_list))
    for country in list: 
        unique_characters = set(country.lower())
        if len(unique_characters) == most_letters:
            country_with_most_letters = country
            final_list.append(country_with_most_letters)
    first_letter_list = (set(country_with_most_letters.lower()))       
    for letter in first_letter_list:
        if letter != " ":
            received_letter_list.append(letter)
    for letter in get_alphabet: 
        if letter not in received_letter_list:
            letters_to_search_for.append(letter)
    def finish_list(letters_to_search, list):
        letter_list_to_work_with = []
        for letter in letters_to_search:
            for country in list: 
                if letter in country:
                    letters_to_search.remove(letter)
                    letter_list_to_work_with = (set(country.lower()))
                    break
            for letter in letters_to_search:
                if letter in letter_list_to_work_with:
                    letters_to_search.remove(letter)
            final_list.append(country)
    for letter in letter_list:
        if len(letters_to_search_for) > 0:
            finish_list(letters_to_search_for, list)
    return final_list


most_vowels(countries)


""" 
alphabet_set(countries)
most_vowels(countries)
alphabet_set(countries)
"""


