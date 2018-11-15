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


def GenerateTrack():
	#generates a regulation standard DIYRobocars track

	track = []
	#straight 1

	for x in np.linspace(0,-2.5,25):
		track.append((x,1))

	# curve 1
	theta = np.linspace(math.radians(270),math.radians(90),100)
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
	theta = np.linspace(math.radians(360),math.radians(270),25)
	center = (6,4)
	rad = 3
	for val in theta:
		xval = rad*math.cos(val)+center[0]
		yval = rad*math.sin(val)+center[1]
		track.append((xval,yval))

	# straight 5
	track.append((0,1))

	return track
'''
track = GenerateTrack()


BLUE = '#0000FF'
BLACK = '#000000'
YELLOW = '#FFFF00'
WHITE = '#000000'

#track = LineString([(0,0),(-10,0),(-10,15),(0,10),(10,15),(10,0),(0,0)])
track = LineString(track)
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
offset_outer = track.parallel_offset(0.75, 'left', join_style=1)
plot_line(ax, offset_outer, color=BLACK)
offset_inner = track.parallel_offset(0.75, 'right', join_style=1)
plot_line(ax, offset_inner, color=BLACK)


ax.set_aspect('equal')
ax.grid(True, which='both')
pyplot.show()
'''