_author_ = 'kiesm'

"""
Function that takes in a file and returns a list of strings for every line
"""
def text_to_list(file):
    file = open(file, 'r')
    freq_list = file.read().splitlines()
    file.close()
    return freq_list

"""
Function that takes in a list of numbers and adds them all together
"""
def add_all_values(list_vals):
    return_num = 0
    for i in list_vals:
        return_num += int(i)
    return return_num

"""
Recursively tries to find the value that happens twice first
"""
def find_frequency_that_happens_twice(start, list_vals, freq_count):
    for i in list_vals:
        start += int(i)
        if start in freq_count:
            return start
        else:
            freq_count[start] = 1
    return find_frequency_that_happens_twice(start, list_vals, freq_count)

"""
Part 1 of day 1
"""
def part_1(data):
    print(add_all_values(data))

"""
Part 2 of day 1
"""
def part2(data):
    print(find_frequency_that_happens_twice(0, data, {}))

"""
Main function to call the functions for part 1 and 2
"""
def main():
    list_values = text_to_list("Frequencies.txt")
    part_1(list_values)
    part2(list_values)

if __name__ == '__main__':
    main()
