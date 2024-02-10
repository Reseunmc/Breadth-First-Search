__author__ = 'Re'

from vertex import *


dictionary={}
#load_graph function to produce the vertex text
def load_graph(file_name):
    file_name="dartmouth_graph.txt"
    in_file =open(file_name,"r" )

    #for loop to populate the dictionary with the name and x/y
    for line in in_file:
        s= line.strip()
        sp= s.split(";")
        sp2=sp[2].split(",")
        vertex=Vertex((sp[0]), int(sp2[0]),int(sp2[1]))
        key=sp[0]
        dictionary[key]=vertex

    in_file.close()
    in_file =open(file_name,"r" )

    #for loop to split the adjacent list list
    for line in in_file:
        s= line.strip()
        sp= s.split(";")
        key=sp[0]
        name=dictionary[key]
        inner_list = sp[1].split(",")

    #nested for loop to strip and append the adjacentcy values to the list
        for i in inner_list:
            i=i.strip()
            object=dictionary[i]
            name.list.append(object)

    #closes file and returns the dictionary
    in_file.close()
    return dictionary
