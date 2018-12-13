# Draws a DIYrobocars regulation track given the coordinates of the track corners
from matplotlib import pyplot
from shapely.geometry import LineString
import math
import numpy as np

# Definition of robocar course
# 1.5 meter wide track
# hairpin has 1.5m outside radius
# 1 gradual turn
# course must fit inside 20x15m box
def getDistance(P1, P2):
	# calculates the distance between two points
	x1 = P1[0]
	y1 = P1[1]
	x2 = P2[0]
	y2 = P2[1]

	return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def getArcLength(theta1,theta2,r):
	# arc length of a circle
	return r*3.14159*math.radians(math.fabs(theta1-theta2))

def drawLine(P1,P2, track, pPerUnit):
	# draws a line in 2D between two points with "pPerUnit" points per unit of length
	l = getDistance(P1,P2)
	x = np.linspace(P1[0],P2[0],l*pPerUnit)
	y = np.linspace(P1[1],P2[1],l*pPerUnit)
	for i in range(0,len(x)):
		track.append((x[i],y[i]))


def GenerateTrack(spaceing = 5):
	#generates a regulation standard DIYRobocars track

	track = []
	# Key Points
	P1 = (0,1)
	P2 = (-2.5,1)
	P3 = (-2.5,14)
	P4 = (2.5,12)
	P5 = (9,14)
	P6 = (9,4)
	P7 = (6,1)

	# straight 1
	drawLine(P1,P2,track, spaceing)
	'''
	l = getDistance(P1,P2)
	for x in np.linspace(0,P2[0],):
		track.append((x,1))
	'''

	# curve 1
	arc1 = getArcLength(270,90,6.5)
	theta = np.linspace(math.radians(270),math.radians(90),arc1*spaceing)
	center = (-2.5,7.5)
	rad = 6.5
	for val in theta:
		xval = rad*math.cos(val)+center[0]
		yval = rad*math.sin(val)+center[1]
		track.append((xval,yval))

	# straight 2
	track.append((2.5,12))

	# straight 3
	track.append((9,14))

	# straight 4
	track.append((9,4))

	# curve 2
	arc2 = getArcLength(360,270,3)
	theta = np.linspace(math.radians(360),math.radians(270),arc2*spaceing)
	center = (6,4)
	rad = 3
	for val in theta:
		xval = rad*math.cos(val)+center[0]
		yval = rad*math.sin(val)+center[1]
		track.append((xval,yval))

	# straight 5
	track.append((0,1))

	return track


def drawTrack(centerline, width = .75):
	# draws the track
	BLUE = '#0000FF'
	BLACK = '#000000'
	YELLOW = '#FFFF00'
	WHITE = '#000000'
	
	track = LineString(centerline)
	#track_bounds = track.bounds
	#ax_range = [int(track_bounds[0] - 1.0), int(track_bounds[2] + 1.0)]
	#ay_range = [int(track_bounds[1] - 1.0), int(track_bounds[3] + 1.0)]

	def plot_coords(ax, x, y, color='#999999', zorder=1):
	    ax.plot(x, y, 'o', color=color, zorder=zorder)

	def plot_line(ax, ob, color='#0000FF', linestyle='-'):
	    parts = hasattr(ob, 'geoms') and ob or [ob]
	    for part in parts:
	        x, y = part.xy
	        ax.plot(x, y, color=color, linewidth=3, solid_capstyle='round', zorder=1, linestyle=linestyle)

	### Plot the track
	# define the figure
	fig = pyplot.figure(1, figsize= [25,20], dpi=90)
	ax = fig.add_subplot(111)

	plot_line(ax, track, BLACK, '--')
	#x, y = list(track.coords)[0]
	#plot_coords(ax, x, y)
	offset_outer = track.parallel_offset(width, 'left', join_style=1)
	plot_line(ax, offset_outer, color=BLACK)
	offset_inner = track.parallel_offset(width, 'right', join_style=1)
	plot_line(ax, offset_inner, color=BLACK)


	ax.set_aspect('equal')
	ax.grid(True, which='both')
	pyplot.show()
	return 1


track = GenerateTrack()

if __name__ == '__main__':
	show = True
	track = GenerateTrack()

	if show:
		drawTrack(track)