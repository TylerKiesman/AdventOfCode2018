_author_ = 'kiesm'

import Day1Code.Day1 as day1

"""
Finds the total amount of squares with 2 or more claims
"""
def find_claims(values, pos_dict):
    overriding_count = 0
    for line in values:
        splited_line = split_line(line)
        starting_x = int(splited_line[1]) + 1
        starting_y = int(splited_line[2]) + 1
        width = int(splited_line[3])
        length = int(splited_line[4])
        for x in range(width):
            for y in range(length):
                position = (starting_x + x, starting_y + y)
                if position in pos_dict and pos_dict[position] == 1:
                    pos_dict[position] += 1
                    overriding_count += 1
                elif position in pos_dict and pos_dict[position] == 2:
                    continue
                else:
                    pos_dict[position] = 1
    return overriding_count

"""
Finds the ID of the only claim that didn't overlap
"""
def find_id(vals, pos_dict):
    for line in vals:
        splited_line = split_line(line)
        starting_x = int(splited_line[1]) + 1
        starting_y = int(splited_line[2]) + 1
        width = int(splited_line[3])
        length = int(splited_line[4])
        num_of_space = width * length
        single_space_counter = 0
        for x in range(width):
            for y in range(length):
                position = (starting_x + x, starting_y + y)
                if position in pos_dict and pos_dict[position] == 1:
                    single_space_counter += 1
                elif position in pos_dict and pos_dict[position] == 2:
                    break
        if single_space_counter == num_of_space:
            return splited_line[0]
    return "There's none."

"""
Splits the line into a tuple with all its components
"""
def split_line(line):
    spaces_split = line.split()
    id = spaces_split[0].split("#")[1]
    from_left = spaces_split[2].split(",")[0]
    from_top = spaces_split[2].split(",")[1].split(":")[0]
    width = spaces_split[3].split("x")[0]
    length = spaces_split[3].split("x")[1]
    returned_line = (id, from_left, from_top, width, length)
    return returned_line

"""
Function for part 1 of day 3
"""
def part_1(data, dictionary):
    print(find_claims(data, dictionary))

"""
Function for part 2 of day 3
"""
def part_2(data, dictionary):
    print(find_id(data, dictionary))

"""
Main function to call the functions for part 1 and 2
"""
def main():
    vals = day1.text_to_list("fabric.txt")
    dictionary = {}
    part_1(vals, dictionary)
    part_2(vals, dictionary)

if __name__ == "__main__":
    main()