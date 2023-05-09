import matplotlib.pyplot as plt
import numpy as np

# given tables

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
