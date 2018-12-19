_author_ = 'kiesm'

import Day1Code.Day1 as day1

"""
Returns 2 dictionaries for all the data about the guards and when they slept
"""
def find_sleep_data(lines):
    each_min_counter = {}
    total_min_asleep = {}
    guard = None
    fall_asleep = None
    for line in lines:
        split_line = line.split()
        time = split_line[1][:-1]
        time = int(time.split(':')[1])
        if "Guard" in line:
            guard = int(line.split()[3][1:])
            fall_asleep = None
        elif "falls" in line:
            fall_asleep = time
        elif "wakes" in line:
            for i in range(fall_asleep, time):
                if (guard, i) not in each_min_counter and guard not in total_min_asleep:
                    each_min_counter[(guard, i)] = 1
                    total_min_asleep[guard] = 1
                elif (guard, i) not in each_min_counter and guard in total_min_asleep:
                    each_min_counter[(guard, i)] = 1
                    total_min_asleep[guard] += 1
                else:
                    each_min_counter[(guard, i)] += 1
                    total_min_asleep[guard] += 1
    return each_min_counter, total_min_asleep

"""
Part 1 of day 4
"""
def part_1(data):
    sleepiest_guard = None
    most_time_slept = 0
    for guard in data[1]:
        if data[1][guard] > most_time_slept:
            most_time_slept = data[1][guard]
            sleepiest_guard = guard
    most_min_slept = 0
    min = 0
    for i in data[0]:
        if i[0] == sleepiest_guard:
            if data[0][i] > most_min_slept:
                most_min_slept = data[0][i]
                min = i[1]
    print(sleepiest_guard * min)

"""
Part 2 of day 4
"""
def part_2(data):
    sleepiest_guard = None
    most_min_slept = 0
    min = 0
    for i in data[0]:
        if data[0][i] > most_min_slept:
            most_min_slept = data[0][i]
            min = i[1]
            sleepiest_guard = i[0]
    print(sleepiest_guard * min)

"""
Main function to call the functions for part 1 and 2
"""
def main():
    vals = day1.text_to_list("record.txt")
    vals.sort()
    sleeping_data = find_sleep_data(vals)
    part_1(sleeping_data)
    part_2(sleeping_data)

if __name__ == "__main__":
    main()