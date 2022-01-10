import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.animation import FuncAnimation
from time import sleep
#%matplotlib qt

fig = plt.figure(figsize=(8,6))
axes = fig.add_subplot(1,1,1)
axes.set_ylim(0, 150)

%matplotlib qt


lst1 = ['a', 'b', 'c', 'd', 'e']
lst2 = [3, 0, 2, 1, 4]

y1=[]
y2=[]

def animate(i):
    y1=lst1[i]
    y2=lst2[i]

    plt.bar(["one", "two"], [y1,y2])

    ani = FuncAnimation(fig, animate, interval=100)

for i in range(len(lst1)):
    animate(i)

'''for i in x:
    sleep(1)
    print(i)'''





















'''# importing libraries
import numpy as np
import time
import matplotlib.pyplot as plt

# creating initial data values
# of x and y
x = np.linspace(0, 10)
y = np.sin(x)

# to run GUI event loop
plt.ion()

# here we are creating sub plots
figure, ax = plt.subplots(figsize=(10, 8))
line1, = ax.plot(x, y)

# setting title
plt.title("Geeks For Geeks", fontsize=20)

# setting x-axis label and y-axis label
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Loop
for _ in range(50):
	# creating new Y values
	new_y = np.sin(x-0.5*_)

	# updating data values
	line1.set_xdata(x)
	line1.set_ydata(new_y)

	# drawing updated values
	figure.canvas.draw()

	# This will run the GUI event
	# loop until all UI events
	# currently waiting have been processed
	figure.canvas.flush_events()

	time.sleep(0.1)
'''