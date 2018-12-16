_author_ = 'kiesm'

import Day1Code.Day1 as day_1

"""
Find the checksum for the values
"""
def find_checksum(vals):
    num_of_two = 0
    num_of_three = 0
    for word in vals:
        searching_for_two = True
        searching_for_three = True
        word_dict = {}
        word_list = list(word)
        for letter in word_list:
            if letter in word_dict:
                word_dict[letter] += 1
            else:
                word_dict[letter] = 1
        for key in word_dict:
            if word_dict[key] == 2 and searching_for_two:
                num_of_two += 1
                searching_for_two = False
            elif word_dict[key] == 3 and searching_for_three:
                num_of_three += 1
                searching_for_three = False
    return num_of_three * num_of_two

"""
Finds the similar words with only one letter different
"""
def find_similar_word(vals):
    for word in vals:
        copied_list = vals[:]
        for copy in copied_list:
            word_idx = 0
            if copy == word:
                continue
            compared_word = list(copy)
            word_as_list = list(word)
            if len(compared_word) != len(word_as_list):
                continue
            only_missing_idx = -1
            while word_idx < len(compared_word):
                if compared_word[word_idx] != word_as_list[word_idx] and only_missing_idx == -1:
                    only_missing_idx = word_idx
                    word_idx += 1
                elif compared_word[word_idx] == word_as_list[word_idx]:
                    word_idx += 1
                    if word_idx == len(compared_word) and only_missing_idx != -1:
                        del(word_as_list[only_missing_idx])
                        return "".join(word_as_list)
                else:
                    break
    return "There's no words that match."

"""
Function for part 1 of day 2
"""
def part_1(data):
    print(find_checksum(data))

"""
Function for part 2 of day 2
"""
def part_2(data):
    print(find_similar_word(data))

"""
Main function to call the functions for part 1 and 2
"""
def main():
    init_vals = day_1.text_to_list("IDs.txt")
    part_1(init_vals)
    part_2(init_vals)

if __name__ == '__main__':
    main()