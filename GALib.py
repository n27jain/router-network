import pygad

# given n number of devices 
# given nxn matrix of distances 
# given that T is (X0 device) connected to all others

# for each soltion (theta1, theta2, theta3 ... thetaN) (where N is the device number)
# convert to cartisean coordinates (x1,y1) ... (xN, yN)
# for each row, check and see if its connects are fairly distanced (cartesian distances)
# fitness = sumofall( distances missed | absolute value |)