_author_ = 'kiesm'

import Day1Code.Day1 as day1

"""
Split each line up into a tuple that contains the steps that must come before each other step
"""
def split_lines(lines):
    step_orders = []
    for line in lines:
        step_order = (line[5], line[36])
        step_orders.append(step_order)
    return step_orders

"""
Creates a 'graph' of nodes given a list of tuples that all contain steps of a graph
"""
def make_graph(steps):
    graph = {}
    pre_reqs = {}
    for step in steps:
        if step[1] not in pre_reqs:
            pre_list = []
            pre_list.append(step[0])
            pre_reqs[step[1]] = pre_list
        else:
            pre_reqs[step[1]].append(step[0])
        if step[0] not in graph:
            new_list = []
            new_list.append(step[1])
            graph[step[0]] = new_list
        else:
            graph[step[0]].append(step[1])
    return graph, pre_reqs

"""
Checks if a node can continue on to the next
"""
def can_continue(node, pre_reqs, path):
    if node not in pre_reqs:
        return True
    pre_nodes = pre_reqs[node]
    for node in pre_nodes:
        if node not in path:
            return False
    return True

"""
Finds the path of a given graph
"""
def find_path(graph, pre_reqs, available, path):
    if len(available) == 0:
        return path
    available.sort()
    for node in available:
        if can_continue(node, pre_reqs, path):
            path.append(node)
            if node not in graph:
                return path
            for i in graph[node]:
                if i not in available:
                    available.append(i)
            available.remove(node)
            find_path(graph, pre_reqs, available, path)
    return path

"""
Finds the first few available nodes in a graph
"""
def find_available(graph, pre_reqs):
    available_nodes = []
    for node in graph:
        if node not in pre_reqs:
            available_nodes.append(node)
    return available_nodes

"""
Part 1 of day 7
"""
def part_1(data):
    steps = split_lines(data)
    graph, pre_reqs = make_graph(steps)
    available = find_available(graph, pre_reqs)
    s = ""
    path = find_path(graph, pre_reqs, available, [])
    print(s.join(path))
    return path, pre_reqs

"""
Part 2 of day 7
"""
def part_2(path, pre_reqs):
    print()

"""
Main function to call the functions for part 1 and 2
"""
def main():
    steps = day1.text_to_list("steps.txt")
    path, pre_reqs = part_1(steps)
    part_2(path, pre_reqs)

if __name__ == "__main__":
    main()