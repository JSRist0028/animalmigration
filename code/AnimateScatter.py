# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 11:24:31 2021

@author: Justin Rist
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# change following links to select data to graph

data = pd.read_csv('https://raw.githubusercontent.com/JSRist0028/animalmigration/main/longtest_y.csv', header = None)
data2 = pd.read_csv('https://raw.githubusercontent.com/JSRist0028/animalmigration/main/data/testing_y.csv', header = None)

fig = plt.figure()
ax = plt.axes(xlim=(50, 75), ylim=(0, 60))
line = ax.scatter([], [], c = 'orange')
line2 = ax.scatter([], [], c = 'blue')

def init():
    return line, line2

def animate(i):
    x = data[0][i-10:i]
    y = data[1][i-10:i]
    
    x2 = data2[0][i-10:i]
    y2 = data2[1][i-10:i]
    
    line = ax.scatter([x], [y], c = 'orange')
    line2 = ax.scatter([x2], [y2], c = 'blue')
    return line, line2

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=100, interval=100, blit=True)

plt.legend(['predicted', 'actual'])
plt.title('Predicted v. Actual Animal Location')
plt.xlabel('Latitude')
plt.ylabel('Longitude')
plt.show()   