# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 11:09:36 2019

@author: 201289902
"""

# Scrapes data from web

import requests
import bs4

r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
td_zs = soup.find_all(attrs={"class" : "z"})

print(td_ys)
print(td_xs)
print(td_zs)


import matplotlib
matplotlib.use('TkAgg')

import random
import operator
import matplotlib.pyplot
import matplotlib.animation
import agentframework_v3
import csv
import tkinter

# Defines the distance between agents
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) +
        ((agents_row_a.y - agents_row_b.y)**2))**0.5



# Connects model to external agent
#a = agentframework_v2.Agent(environment)
## print(a.y, a.x)
#a.move()
#print(a.y, a.x)

# Makes the environment for the agents.  Imports data to use as our agents' environment, and gets them to interact with it
f = open('in.txt', newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
environment = []
for row in reader:				
    rowlist = []
    for value in row:				
        rowlist.append(value)   
    environment.append(rowlist)  


# Makes the agents.  for agent file use filename.  if agent framework filename changes, change append statement

num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20
agents = []


for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    z = int(td_zs[i].text)
    agents.append(agentframework_v3.Agent(environment, agents, y, x, z))


# Moves the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):

#        if random.random() < 0.5:
#            agents[i][0] = (agents[i][0] + 1) % 100
#        else:
#            agents[i][0] = (agents[i][0] - 1) % 100
#
#        if random.random() < 0.5:
#            agents[i][1] = (agents[i][1] + 1) % 100
#        else:
#            agents[i][1] = (agents[i][1] - 1) % 100
        
# Agents interacting with environment
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
        

# Dislays the agents
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
#    matplotlib.pyplot.show()


# Agent Distance Loop related to code in Line 13
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
       
        
        
# Animates the model
        
#        
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1,1])

#ax.set_autoscale_on(False)

def update(frame_number):

    fig.clear()   
#
    for i in range(num_of_agents):
        y = int(td_ys[i].text)
        x = int(td_xs[i].text)
        agents.append(agentframework_v3.Agent(environment))


# Moves the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):

#        if random.random() < 0.5:
#            agents[i][0] = (agents[i][0] + 1) % 100
#        else:
#            agents[i][0] = (agents[i][0] - 1) % 100
#
#        if random.random() < 0.5:
#            agents[i][1] = (agents[i][1] + 1) % 100
#        else:
#            agents[i][1] = (agents[i][1] - 1) % 100
        
# Agents interacting with environment
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
        

# Dislays the agents
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
#    matplotlib.pyplot.show()


# Agent Distance Loop related to code in Line 13
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)

#animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)
#matplotlib.pyplot.show()

        
# Adds a GUI for the matplotlib graphic.  IPython prompt must be set to Tkinter

    
# creates a menu window for the animation. 
root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

def run():
    pass
    
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)

tkinter.mainloop()



        