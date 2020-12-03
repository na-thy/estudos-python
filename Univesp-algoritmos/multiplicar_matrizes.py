import numpy as np
A = np.array ([[0,1,0,0],[0,0,1,0],[1,0,0,0],[0,0,1,1]])

B = np.array ([[0,1,0,0],[0,0,1,0],[1,0,0,0],[0,0,1,1]])

C = np.array ([[0,1,0,0],[0,0,1,0],[1,0,0,0],[0,0,1,1]])

D = np.array ([[0,1,0,0],[0,0,1,0],[1,0,0,0],[0,0,1,1]])

AB = A.dot(B)
ABC = AB.dot(C)
ABCD = ABC.dot(D)

print('multiplicação')

print(ABCD)