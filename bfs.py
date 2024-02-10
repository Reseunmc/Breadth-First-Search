__author__ = 'Re'

from load_graph import *
from collections import *


def breadth_first_search(start_vertex, goal_vertex):
    back_pointer={}
    queue=deque()

#appends the start vertex to back pointer
    queue.append(start_vertex)
    back_pointer[start_vertex]=None

#if the queue has an item in it, proceed
    while len(queue)>0:

#deletes the item from the queue
        x=queue.popleft()

# runs through the list and sets the adjacent vertex to x
        for adjacent in x.list:
            if not adjacent in back_pointer:
                back_pointer[adjacent]= x
                queue.append(adjacent)

#If the goal vertex is the adjacent backpointer make a new list and append x to the new path
        if x==goal_vertex:
            new_path=[]
            while x!=None:
                new_path.append(x)
                x=back_pointer[x]
            return new_path
