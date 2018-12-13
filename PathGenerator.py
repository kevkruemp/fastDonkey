#Artificial driver agent
import time
import math
import path
import DrawTrack
import numpy as np

# Basic Design
# (1) set the starting point 0
# (2) for eahc point i, decide the point i+1 using the algorithm
# (3) run many times and select the best "path"

# Car Dynamics
K_max = 1  # maximum curvature of car 1/minimum turning radius
V_max = 10 # maximum velocity in m/s
A_max = .5 # maximum acceleration rate in g's
A_min = -1 # maximum deceleration rate in g's


def Optimize(numIterations, debug = False):
	# base for the optimizer

	# Initialize
	currIt = 0
	centerline = path.Path(DrawTrack.GenerateTrack())
	start = centerline.path[0] # we start in the middle of the track


	new_path = path.Path()

	for i in range(0,len(centerline)-2):
		new_point = generate_Point(centerline,i)
		new_path.append_point(new_point)

	#print(centerline.curvature)

#driver algorithm

# define car dynamics
	# kv^2 - ug <=0    car will not slip
	# integral of k*ds = delta_theta
	# k <= k_max       all turns must be doable by the car
	# v <=  v_max      
	# a <= a_max       car can accelerate as requested
	# a >= a_min       car can DEcelerate as requested

# grab and process center line

# choose starting point

# define linear probability field
def calc_probability_field(k, k1, k2):
	# look at the next 2 points on the center line, find their curvatures k1 and k2
	s = min(max(k2-k1/MaxK, -1), 1)

	p = random() # Generate random number between 0 and 1
	ds = (-1 + math.sqrt(1-s*(2-s-4*p)))/s

	# s = min(max(k2-k1/MaxK, -1),1)
	# define probability as y = .5 + .5*s*x
	# pick random number 0 <= p <=1 
	# ds value comes out as -1 + sqrt(1-s*(2-s-4*p)) all divided by s

	# Where ds is the distance from the centerline normal to the line
	return ds

def generate_Point(centerline, index):
	# generates a new point using a weighted linear probability field
	ds = calc_probability_field(centerline.curvature[index],centerline.curvature[index+1],centerline.curvature[index+2])

	new_point = path_to_cartesian(centerline, ds)

	while bad_curvature(path,index):
		# generate a new point until you get one within the required angle bounds
		ds = calc_probability_field(centerline.curvature[index],centerline.curvature[index+1],centerline.curvature[index+2])
		new_point = path_to_cartesian(centerline, ds)

	return new_point


def bad_curvature(path, ind):
	# if angle between selected point and past 2 points is >20 degrees, return false, otherwise true
	angle = path.get_back_angle(ind)
	if angle > 20.0:
		return 1
	else:
		return 0


# check that curvature between current point and past 2 points is not too high, otherwise generate another point


# velocity solver:
	# V(0)=0 at i=0
	# i = i+1
	# choose velocity V(i) based on reachability constraints
		# kv^2 - mu*g <= 0   "car can make the turn without losing grip"
		# v <= Vmax
		# a <= A_max car can accelerate to this value from previous speed
		# a >= A_min car can decelerate to this value from previous speed

	# Choose the largest velocity that meets cornering constraints and acceleration constraint
	# check deceleration constraint, if met I = i+1, if not go to i-1 and reduce the velocity to meet deceleration constriant
		# recursively keep checking previous points until they all satisfy braking constraints
		# this makes sure you brake appropraitely as you approach a sharp turn


# calculate the time cost and E cost for this run.
# time = integral of distance(i, i+1) / v(i,i+1)


#Optimize()

if __name__ == '__main__':
	debug = True

	#Optimize(1, debug)

	test1 = [(-2.5,1),(-9,7.5),(-2.5,14)]
	test = [(0,1),(-1,1)]
	P = path.Path(test)
	P.curvature = [0, 0]
	P.angle = [180, 180]
	P.append_point(test1[0]) # angles added are all positive, needs fixing
	P.append_point(test1[1])
	P.append_point(test1[2])

	print(P.path)
	print(P.curvature)
	print(P.angle)

