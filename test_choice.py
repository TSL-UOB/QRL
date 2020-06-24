import numpy as np
import matplotlib.pyplot as plt

W=3
H=2
size=W*H

prob = np.random.rand(W, H)
# prob[:,2:10] = 0
prob[:,0:1] = 0 #column/row
prob[0:2,:] = 0
prob /= np.sum(prob)
print(prob)
fig = plt.figure(figsize=(W,H)); 

for i in range (50):
	a = np.random.choice(size,1,p=prob.flatten())

	# print("draw is %d " % a)
	x=(int)(np.floor(a/H)) 	#x returns rows 
	y=(int)(a%H) 			#y returns columns
	# x=(int)(np.floor(a%H))#x returns columns
	# y=(int)(a/H) 			#y returns rows
	print("a=%d x=%d y=%d" % (a,x,y))
	input()

	Z=np.zeros(shape=(W,H))
	Z[x,y]=1
	Z = np.rot90(Z,k=1)
	# Z = np.flipud(Z)
	Wx = np.linspace(0, W-1, W)
	Hy = np.linspace(0, H-1, H)
	print("Wx",Wx)
	print("Hy",Hy)
	plt.contourf(Wx,Hy,Z)
	plt.plot(x,y,'kx')		
	plt.pause(.1)
	print(a)
	input()