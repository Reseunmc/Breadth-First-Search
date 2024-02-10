__author__ = 'Re'
from cs1lib import *
from load_graph import *
from bfs import *
WINDOW_HEIGHT=811
WINDOW_WIDTH=1012

#function to draw the map
def draw_map():
    img=load_image("dartmouth_map.png")
    draw_image(img,0,0)

#draws the image
def image():
    draw_map()
    dictionary = load_graph("dartmouth_graph.txt")

#the start vertex and goal vertex are initially = none
    start_vertex= None
    goal_vertex=None

    while not window_closed():

#loops through the dictionary to draw the intial path in blue
        for key in dictionary:
            dictionary[key].draw_virtices(0,0,1)
            dictionary[key].draw_adjacent_edges(0,0,1)

#if the mouse is down and the mosue coordinate is within the smallest squre around the circle
            if mouse_down() and (dictionary[key].mouse_coord()):
                start_vertex=dictionary[key]

#if the start vertex returns to none draw the vertex in red
            if start_vertex != None:
                start_vertex.draw_virtices(1,0,0)
        goal_vertex=None

#loops through the dictionary
        for key in dictionary:

#the start veretx is equal to none and the the vertex is being hovered over
            if start_vertex!=None and dictionary[key].mouse_coord():

                goal_vertex=dictionary[key]

        if goal_vertex != None:
            goal_vertex.draw_virtices(1,0,0)

#if the starrt and goal vertices are none perform the breadth first search and draw
        if start_vertex!=None and goal_vertex!=None:
            p_list=breadth_first_search(start_vertex,goal_vertex)
            previous=goal_vertex
            for i in p_list:
                i.draw_edge(previous,1,0,0)
                i.draw_virtices(1,0,0)
                previous=i



        request_redraw()
        sleep(.02)
start_graphics(image,"draw_image",WINDOW_WIDTH,WINDOW_HEIGHT)
