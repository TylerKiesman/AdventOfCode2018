_author_ = 'kiesm'

"""
Gets the string that the puzzle is for
"""
def get_line():
    line = open("polymers.txt", 'r')
    return line.readline()

"""
Function that goes through the polymer and goes through all possible 'reactions'
"""
def resulting_polymer_after_reaction(line):
    line_length = len(line)
    i = 0
    j = i + 1
    while j < line_length:
        if ord(line[i]) - ord(line[j]) == 32 or ord(line[j]) - ord(line[i]) == 32:
            first_half_line = line[:i]
            second_half_line = line[j + 1:]
            post_slice_line = first_half_line + second_half_line
            line = post_slice_line
            line_length = len(line)
            if i != 0:
                i -= 1
                j -= 1
        else:
            i += 1
            j = i + 1
    return len(line)

"""
Function for part 2 that finds the shortest possible polymer after removing a certain letter
"""
def shortest_possible_polymer(line):
    shortest_line = -1
    for i in range(ord('a'), ord('z')):
        formatted_line = line.replace(chr(i), '')
        formatted_line = formatted_line.replace(chr(i - 32), '')
        current_line_length = resulting_polymer_after_reaction(formatted_line)
        if current_line_length < shortest_line or shortest_line == -1:
            shortest_line = current_line_length
    print(shortest_line)

"""
Part 1 of day 5
"""
def part_1(line):
    print(resulting_polymer_after_reaction(line))

"""
Part 2 of day 5
"""
def part_2(line):
    shortest_possible_polymer(line)

"""
Main function to call the functions for part 1 and 2
"""
def main():
    part_1(get_line())
    part_2(get_line())

if __name__ == "__main__":
    main()