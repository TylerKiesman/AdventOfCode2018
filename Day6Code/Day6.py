_author_ = 'kiesm'

import Day1Code.Day1 as day1

"""
Takes lines of points and transforms them into tuples to represent points
"""
def data_to_points(data):
    points = []
    for line in data:
        split_line = line.split()
        x = int(split_line[0].split(',')[0])
        y = int(split_line[1])
        point = (x, y)
        points.append(point)
    return points

"""
Find the max x value out of a list of points
"""
def find_x_max(points):
    x_max = 0
    for point in points:
        if point[0] > x_max:
            x_max = point[0]
    return x_max

"""
Find the max y values out of a list of points
"""
def find_y_max(points):
    y_max = 0
    for point in points:
        if point[1] > y_max:
            y_max = point[1]
    return y_max

"""
Find the manhattan distance of two points
"""
def find_manhattan_distance(point_1, point_2):
    horizontal_distance = abs(point_1[0] - point_2[0])
    vertical_distance = abs(point_1[1] - point_2[1])
    manhattan_distance = horizontal_distance + vertical_distance
    return manhattan_distance

"""
Finds the largest area that isn't infinite
"""
def find_largest_non_inifite(points, x_max, y_max):
    coordinate_count = {}
    for point in points:
        coordinate_count[point] = 0
    x_idx = 0
    while x_idx <= x_max:
        y_idx = 0
        while y_idx <= y_max:
            current_point = (x_idx, y_idx)
            shortest_dist = None
            shortest_point = None
            for point in points:
                man_distance = find_manhattan_distance(current_point, point)
                if man_distance == shortest_dist:
                    continue
                if shortest_dist == None or man_distance < shortest_dist:
                    shortest_dist = man_distance
                    shortest_point = point
            if current_point[0] == 0 or current_point[1] == 0 or current_point[0] == x_max or current_point[1] == y_max:
                coordinate_count[shortest_point] = "Infinite"
            if coordinate_count[shortest_point] != "Infinite":
                coordinate_count[shortest_point] += 1
            y_idx += 1
        x_idx += 1
    largest_count = 0
    for coord in coordinate_count:
        if coordinate_count[coord] != "Infinite" and coordinate_count[coord] > largest_count:
            largest_count = coordinate_count[coord]
    print(largest_count)

"""
Finds the size of the region containing all locations which have a total distance to all given coordinates of 
less than 10000
"""
def find_regions_within_distance(points, x_max, y_max, max_distance):
    safe_region_count = 0
    x_idx = 0
    while x_idx <= x_max:
        y_idx = 0
        while y_idx <= y_max:
            current_point = (x_idx, y_idx)
            total_distances = 0
            for point in points:
                total_distances += find_manhattan_distance(current_point, point)
            if total_distances < max_distance:
                safe_region_count += 1
            y_idx += 1
        x_idx += 1
    print(safe_region_count)

"""
Part 1 of day 6
"""
def part_1(points):
    x_max = find_x_max(points)
    y_max = find_y_max(points)
    find_largest_non_inifite(points, x_max, y_max)

"""
Part 2 of day 6
"""
def part_2(points):
    x_max = find_x_max(points)
    y_max = find_y_max(points)
    find_regions_within_distance(points, x_max, y_max, 10000)

"""
Main function to call the functions for part 1 and 2
"""
def main():
    point_data = day1.text_to_list("points.txt")
    points = data_to_points(point_data)
    part_1(points)
    part_2(points)

if __name__ == "__main__":
    main()