import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import json
import math

from random import randrange
# given tables


jsonstring = '{"newObj":{"A":{"routes":[{"toDeviceID":"A","RSSID":0},{"toDeviceID":"B","RSSID":1.5},{"toDeviceID":"C","RSSID":3},{"toDeviceID":"D","RSSID":4}]},"B":{"routes":[{"toDeviceID":"A","RSSID":1.5},{"toDeviceID":"B","RSSID":0},{"toDeviceID":"C","RSSID":2},{"toDeviceID":"D","RSSID":3}]},"C":{"routes":[{"toDeviceID":"A","RSSID":3},{"toDeviceID":"B","RSSID":2},{"toDeviceID":"C","RSSID":0},{"toDeviceID":"D","RSSID":4.9}]},"D":{"routes":[{"toDeviceID":"A","RSSID":4},{"toDeviceID":"B","RSSID":3},{"toDeviceID":"C","RSSID":4.9},{"toDeviceID":"D","RSSID":0}]}}}'
data = json.loads(jsonstring)

def convertTo2DArray(data):
    newData = {}
    for key in data["newObj"]:
        left = key
        list = data["newObj"][key]["routes"]
        for value in list:
            right = value["toDeviceID"]
            distance = value["RSSID"]
            if left in newData:
                newData[left][right] = distance
            else:
                newEntry = {}
                newEntry[right] = distance
                newData[left] = newEntry
            if right in newData:
                newData[right][left] = distance
            else:
                newEntry = {}
                newEntry[left] = distance
                newData[right] = newEntry
    return newData

data = convertTo2DArray(data)


print(data)
#[]:A": {
# 			"routes": [
# 				{
# 					"toDeviceID": "A",
# 					"RSSID": 0
# 				},
# 				{
# 					"toDeviceID": "B",
# 					"RSSID": 10000
# 				},
# 				{
# 					"toDeviceID": "C",
# 					"RSSID": 5000
# 				}
# 			]
# 		},


array = ''



# Pick table[0]. Set it to (0,0) {A}
# select 2 edges on it {B,C}. then search for edge B->C
# if AB + AC > BC && AC + BC > AB && AB + BC > AC ( This is a valid triangle and now use law of sine )

# using trig, find the 2 new AP relative position on the graph.

# if the sum of to sides us larger than the third we have to possible solutions.

#1.) Average down one of the sides and then apply law of sines
#2.) one of the AP is in between 2 others and so it is a straight line. (unless there is an edge case that I may be missing)



# test

# A - B 1.5
# A - C 3
# A - D 4

# B - A 1.5
# B - C 2
# B - D 3

# C - A 3
# C - B 2
# C - D 4.9

# D - A 4
# D - B 3
# D - C 4.9

# def createEdges():
#     edges = [['A', 'B'],['A', 'C'], ['A', 'D'] ['B', 'C'], ['B', 'D'], ['C', 'D']]
#     G = nx.Graph()
#     G.add_edges_from(edges)
#     pos = nx.spring_layout(G)
#     plt.figure()
#     nx.draw(
#         G, pos, edge_color='black', width=1, linewidths=1,
#         node_size=500, node_color='pink', alpha=0.9,
#         labels={node: node for node in G.nodes()}
#     )
#     nx.draw_networkx_edge_labels(
#         G, pos,
#         edge_labels={('A', 'B'): 'AB', 
#                     ('B', 'C'): 'BC', 
#                     ('B', 'D'): 'BD',
#                     ('A', 'C'): 'AB', 
#                     ('A', 'D'): 'BC', 
#                     ('C', 'D'): 'BD'},
#         font_color='red'
#     )
#     plt.axis('off')
#     plt.show()

# createEdges()

# tables = []
# def determinePos():
#     size = len(tables)
#     lookUpPos = []

#     start = tables[0]
#     lookUpPos[0]= [star]


def compute(data):
    # create a new dict where each AP has a defined x,y coordinate

    pos = {}
    for key in data:
        if len(pos) == 0:
            pos[key] = (0,0)
        else:
            collected = []
            for stackey in pos:
                if data[key][stackey] > 0:
                    collected.append([stackey, data[key][stackey] ])
                if len(collected) == 2:
                    A = collected[0][0]
                    me_A = collected[0][1]
                    B = collected[1][0]
                    me_B = collected[1][1]
                    A_B = data[A][B]
                    # solve for me
                    
                    if(me_A + me_B > A_B and me_A + A_B > me_B and me_B + A_B > me_A): # follows the law of triangle sides
                        a = me_A
                        b = me_B
                        c = A_B
                        angle_c = math.acos((a^2 + b ^ 2 - c ^ 2 )/ (2 *  a * B))
                        A_pos = pos[A]
                        B_pos = pos[B]
                        X = A_pos[0] + me_A * math.sin(angle_c)
                        Y = A_pos[1] + me_A * math.cos(angle_c)
                        pos[key] = (X,Y)
                    else:
                        print("Error. Valid Triange not discovered")


            if len(collected) == 1:
                # choose any arbitrary direction and plot the distance from point stack [0]
                stackey = collected[0][0]
                friendPos = pos[stackey]
                distance =  collected[0][1]
                myPos = friendPos
                select = randrange(3)
                if select == 0 : myPos[0] += data[key][stackey]
                elif select == 1 : myPos[0] -= data[key][stackey]
                elif select == 2 : myPos[1] += data[key][stackey]
                elif select == 3 : myPos[1] -= data[key][stackey]
                pos[key] = myPos

    print(pos) 
            




