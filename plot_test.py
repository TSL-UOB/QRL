import matplotlib.pyplot as plt
from drawnow import drawnow
import numpy as np
import random
from matplotlib.animation import FuncAnimation, PillowWriter 
from celluloid import Camera
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.animation as animation

def energyField_update(nA,nExp,agentState,indexID,indexIDbool,Ef_Z,gridH,Ef_Log,diag):
	if(diag):print("Agent state for Exp# %d " % nExp)
	if(diag):print("... after randomStart is: ", agentState[0])
	if(diag):print("Agent to generate successful test has ID %d " % indexID[0])
	# inspect each agent and update field inc +ve and -ve
	for agentID in range(0,nA):
		if indexIDbool[agentID]: #which agent generated the test
			valid_start = agentState[0,agentID]
			valid_y = random.randint(0,11)
			valid_x = random.randint(0,65)
			# valid_x = (int)(valid_start[1])
			# valid_y = gridH - (int)(valid_start[0]) -1
			Ef_Z[valid_y,valid_x] -= 1 #reduce energy for good tests
			# Ef_Log.write("%d, %d \n" % (valid_x,valid_y))

def animate(i):
    arr = frames[i]
    vmax     = np.max(arr)
    vmin     = np.min(arr)
    levels   = np.linspace(vmin, vmax, 200, endpoint = True)
    cf = ax.contourf(arr, vmax=vmax, vmin=vmin, levels=levels)
    cax.cla()
    fig.colorbar(cf, cax=cax)
    tx.set_text('Frame {0}'.format(i))


# plt.ion()  # enable interactivity
# fig = plt.figure()  # make a figure

x = list()
y = list()
gridH = 12
gridW = 66
agentBehaviour = 'test_plot'
display_chart_modulo = 10

energyField_xvals = np.linspace(0, gridW, gridW)
energyField_yvals = np.linspace(0, gridH, gridH)
Ef_X, Ef_Y = np.meshgrid(energyField_xvals, energyField_yvals)
Ef_Z = np.zeros(shape=(gridH,gridW))
fig = plt.figure(figsize=(10,4))
# camera = Camera(Ef_fig)
# fig = plt.figure()
ax = fig.add_subplot(111)
div = make_axes_locatable(ax)
cax = div.append_axes('right', '5%', '5%')
frames = []

agentChoices = ['RandAction', 'RandBehaviour','Proximity','Election','Q_Agent']
agentBehaviour = agentChoices[1] 	# TODO replace with CL arg
done=True
plotContour=True
nTests=51
video_pau1e=False
nA=3
maxT=10
agentState = np.empty(shape=(maxT,nA,2))
indexID=[1]
indexIDbool=[True,False,True]
Ef_Log='Ef_Log'
diag=False

import time

for nExp in range(nTests):
	energyField_update(nA,nExp,agentState,indexID,indexIDbool,Ef_Z,gridH,Ef_Log,diag)
	if done:
		frames.append(Ef_Z)
		# display new energy grid (contour plot)
		# if plotContour and (nExp%display_chart_modulo==0):
		# 	print(plotContour)
		# 	print(nExp)
		# 	print(display_chart_modulo)
		# 	print(nExp%display_chart_modulo)
		# 	# raw_input()
		# 	plt.style.use('classic')
		# 	cp = plt.contourf(Ef_X, Ef_Y, Ef_Z)
		# 	plt.colorbar(cp)
		# 	plt.xlabel('x (m)') 
		# 	plt.ylabel('y (m)') 
		# 	plt.title('Initial location energy field: %s run %d of %d' % (agentBehaviour,nExp,nTests-1))	
		# 	if(video_pause) and (nExp==1):raw_input("Camera Ready, press Enter to continue...")
		# 	plt.pause(0.01)
		# 	camera.snap()
		# 	time.sleep(0.1)
		# 	# plt.clf()
			# if plotContour and SaveCharts and (nExp%display_chart_modulo==0):	
			# if SaveCharts:	
			# name_file = "plots/Ef_%s_%d.png" % (agentBehaviour, nExp)
			# print(name_file)
			# plt.savefig(name_file)

			# raw_input("press enter to continue")
			# input("press enter to continue")

cv0 = frames[0]
# cf = ax.contourf(cv0, 200)
cf = ax.contourf(cv0)
# cb = fig.colorbar(cf, cax=cax)
tx = ax.set_title('Frame 0')
ani = animation.FuncAnimation(fig, animate, frames=10)
ani.save('animation.gif', writer='imagemagick', fps=2)
# plt.show()

# animation = camera.animate()
# animation.save('celluloid_minimal.gif', writer = 'imagemagick') 