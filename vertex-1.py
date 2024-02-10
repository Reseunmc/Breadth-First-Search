__author__ = 'Re'
from cs1lib import *

VERTEX_RADIUS=5
EDGE_WIDTH=2
class Vertex:
    def __init__(self,name,x,y):
        self.name=name
        self.x=x
        self.y=y
        list=[]
        self.list=list


#draws the virtices
    def draw_virtices(self,r,g,b):
        set_fill_color(r,g,b)
        draw_circle(self.x,self.y,VERTEX_RADIUS)

#draws the edges
    def draw_edge(self, vertex,r,g,b):
        enable_stroke()
        set_stroke_color(r,g,b)
        set_stroke_width(EDGE_WIDTH)
        draw_line(self.x,self.y,vertex.x,vertex.y)


#draws the edges initially
    def draw_adjacent_edges(self,r,g,b):
        enable_stroke()
        set_stroke_color(r,g,b)
        set_stroke_width(EDGE_WIDTH)
        for i in range (0,len(self.list)):
            draw_line(self.x, self.y, self.list[i].x,self.list[i].y)


#loop through and draw lines betwwen eac
    def mouse_coord(self):
        if mouse_x()>self.x-VERTEX_RADIUS and mouse_x()<self.x+VERTEX_RADIUS and mouse_y()>self.y-VERTEX_RADIUS and mouse_y()<self.y+VERTEX_RADIUS:
            return True
        else:
            return False

#string function to properly add the last adjacent vertex to the vertextxt
    def __str__(self):

#empty string populated by the index of the list
        string=""
        for i in range (0,len(self.list)-1):
            string+=self.list[i].name + ", "
        string+=self.list[-1].name+ "."
        return str(self.name)+"; Location: "+str(self.x)+", "+str(self.y)+":" +"Adjacent Vertices: " +str(string)
