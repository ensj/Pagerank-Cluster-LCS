import numpy as np 
import matplotlib.pyplot as plt 

A = np.array([[0.995,  -0.1], 
			  [0.1,   0.995]])
B = np.array([[1,   -0.1], 
			  [0.1, 0.99]])
C = np.array([[0.99,   -0.1], 
			  [0.1, 0.99]])
P_inv = np.array([[0,     1], 
				  [1, -0.05]])
x = np.array([[1], 
			  [2]])

def expMatMul(A, x, power):
	result = [[], []]
	point = np.matmul(A,x)
	result[0].append(point[0])
	result[1].append(point[1])
	for x in range(1,power):
		point = np.matmul(A, np.array([result[0][x-1], result[1][x-1]]))
		result[0].append(point[0])
		result[1].append(point[1])
	return result

result = expMatMul(C,x,100)
#part 2
"""for x in range(0, 100):
	point = np.matmul(P_inv, np.array([result[0][x],result[1][x]]))
	result[0][x] = point[0]
	result[1][x] = point[1]"""

plt.scatter(result[0], result[1]);

plt.gca().set(xlim=(-5,5),ylim=(-5,5))
plt.axis('square')
plt.show()