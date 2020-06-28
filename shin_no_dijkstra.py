import os
from collections import deque
from tkinter import filedialog

INFINITY = float("inf")


class Graph:
    def __init__(self, filename):
        # Define the network topology as a list
        network = []
        # Walk over the file lines
        with open(filename) as f:
            for line in f:
                # Define the rule of creating the link between nodes from file
                Link = line.strip().split(" ")
                Start_Node, End_Node, cost = Link
                # Adding the file links description to generate the topology
                network.append((Start_Node, End_Node, int(cost)))

        self.nodes = set()
        for node in network:
            self.nodes.update([node[0], node[1]])

        self.adjacency_list = {node: set() for node in self.nodes}
        for node in network:
            self.adjacency_list[node[0]].add((node[1], node[2]))


    def shortest_path(self, start_node, end_node):

        unvisited_nodes = self.nodes.copy()

        distance_from_start = {
            node: (0 if node == start_node else INFINITY) for node in self.nodes
        }

        

        previous_node = {node: None for node in self.nodes}

        while unvisited_nodes:
            current_node = min(
                unvisited_nodes, key=lambda node: distance_from_start[node]
            )
            unvisited_nodes.remove(current_node)

            if distance_from_start[current_node] == INFINITY:
                break

            for neighbor, distance in self.adjacency_list[current_node]:
                atarashi_pathu = distance_from_start[current_node] + distance
                if atarashi_pathu < distance_from_start[neighbor]:
                    distance_from_start[neighbor] = atarashi_pathu
                    previous_node[neighbor] = current_node

            if current_node == end_node:
                break

        path = deque()
        current_node = end_node
        while previous_node[current_node] is not None:
            path.appendleft(current_node)
            current_node = previous_node[current_node]
        path.appendleft(start_node)

        return path, distance_from_start[end_node]
        



def main():
    start = input("Type start node: ")
    end = input("Type end node: ")
    verify_algorithm(
        filename="shin_no_djikstra_graph.txt",
        start= str(start),
        end= str(end),
    )
# path, distance
def verify_algorithm(filename, start, end):
    # Connect the graph class with the network nodes file
    graph = Graph(filename)
    returned_path, returned_distance = graph.shortest_path(start, end)
    print('        shortest path: {0}'.format(returned_path))
    print('       total cost: {0}'.format(returned_distance))

def get_the_node_table():
    file = "shin_no_djikstra_graph.txt"
    f = open(file, "r")
    lines = f.readlines()
    result = []
    for line in lines:
        result.append(line.split(' ')[0])
    # Remove duplication
    resulted = list(dict.fromkeys(result))
    
    f.close()
    return resulted


def check_for_all_nodes(filename, start, end):
    graph = Graph(filename)
    returned_path, returned_distance = graph.shortest_path(start, end)
    #print('      form/to nodes: {0} -> {1}'.format(start, end))
    print('       shortest path: {0}'.format(returned_path))
    print('       total cost: {0}'.format(returned_distance))


if __name__ == "__main__":
    Terminal_profile = """\n
                          #####################################################################################
                          ##                                                                                 ##
                          ##                         CN 5201 Advanced Network Systems                        ##
                          ##                                                                                 ##
                          ##                   Shortest Path Routing Algorithm implementaion                 ##
                          ##                                                                                 ##
                          ##                                                                                 ##
                          #####################################################################################"""
    print(Terminal_profile)
    while True:
        option = input("""\n
        1: to produce the shortest between two desired nodes: \n
        2: To produce the routing table of shortest possible paths for one node: 
        \n
        Enter one of the following options: """)
        if option == "1":
            print("\n##########################################################################\n")
            main()
        #get_the_node_table()
        elif option == "2":
            print("\n##########################################################################\n")
            start = input("Type desired node to get it's possible shortest path:  \n Note that you should use capitalized letters")
            end = get_the_node_table()
            for i in end:
                check_for_all_nodes(
                        filename="shin_no_djikstra_graph.txt",
                        start=str(start),
                        end=str(i)
                    )
        else:
            print("\n##########################################################################\n")
            print('Please enter a valid option and try agian')


