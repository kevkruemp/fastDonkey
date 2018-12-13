# path object
import math
import numpy as np

class Path(object):

	def __init__(self, point_list=[]):
		self.path = point_list
		self.curvature = []
		self.angle = []
		self.velocity = []
		"""
		self.curvature = np.zeros(len(point_list))
		self.angle = np.zeros(len(point_list))
		self.velocity = np.zeros(len(point_list))
		"""

		if len(self.path) >2:
			self.generate_curvature()

	def get_curvature(self, ind1, ind2, ind3):
		# Calculates the curvature of a point on the path
		#k defined by: K = 2*abs((x2-x1).*(y3-y1)-(x3-x1).*(y2-y1)) ./ ...
  		#sqrt(((x2-x1).^2+(y2-y1).^2)*((x3-x1).^2+(y3-y1).^2)*((x3-x2).^2+(y3-y2).^2));
  		x1 = self.path[ind1][0]
  		y1 = self.path[ind1][1]
  		x2 = self.path[ind2][0]
  		y2 = self.path[ind2][1]
  		x3 = self.path[ind3][0]
  		y3 = self.path[ind3][1]

  		# If the points are in a straight line do not divide
  		K_bot = math.sqrt(((x2-x1)**2+(y2-y1)**2)*((x3-x1)**2+(y3-y1)**2)*((x3-x2)**2 +(y3-y2)**2))
  		if K_bot == 0:
  			return 0

  		K = 2*math.fabs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))/K_bot
  		return K

	def generate_curvature(self):
  		# populates the curvature at each point along the list
  		self.curvature[0] = self.get_curvature(0,1,2)
  		for i in range(0,len(self.path)-2):
  			self.curvature[i] = self.get_curvature(i-1,i,i+1)

  		self.curvature[len(self.path)-1] = self.get_curvature(len(self.path)-3,len(self.path)-2,len(self.path)-1)
  		print('done')

	def get_fwd_angle(self, ind):
		# calculates the angle between current point and next point
		a = self.path[ind-1]
		b = self.path[ind]
		c = self.path[ind+1]
		# create vectors
		ab = (b[0]-a[0],b[1]-a[1])
		bc = (c[0]-b[0],c[1]-b[1])
		# dot product
		cosine_angle = np.dot(ab,bc)/(np.linalg.norm(ab)*np.linalg.norm(bc))
		angle = np.arccos(cosine_angle) # angle between vectors in radians

		return np.degrees(angle)

	def get_back_angle(self, ind):
		# calculates the angle between current point and past 2 points
		a = self.path[ind-2]
		b = self.path[ind-1]
		c = self.path[ind]
		# create vectors
		ab = (b[0]-a[0],b[1]-a[1])
		bc = (c[0]-b[0],c[1]-b[1])
		# dot product
		cosine_angle = np.dot(ab,bc)/(np.linalg.norm(ab)*np.linalg.norm(bc))
		angle = np.arccos(cosine_angle) # angle between vectors in radians

		return np.degrees(angle)

	def append_point(self, point):
		# appends a point to the path
		if len(self.path)<2:
			# if path is too short to do angle/curvature calcs just add the point
			self.path.append(point)
		else:
			self.path.append(point)
			ind = len(self.path)-1
			self.curvature.append(self.get_curvature(ind-2,ind-1,ind))
			print(self.get_back_angle(ind))
			self.angle.append(self.angle[ind-1] + self.get_back_angle(ind))

