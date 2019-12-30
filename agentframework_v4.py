# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 11:00:17 2019

@author: 201289902
"""

# This file defines an Agent class. In this scenario, Agents have a location 
# represented by a raster environment which is shared as a list of all other 
# agents with all # other agents in the environment.

import random
environment: list

class Agent():
    
# Initialises an agent.    
    
    def __init__(self, environment,agent, x, y): 
        self.environment = environment
        self.agent = agent
        self.store = 0
        
# Postional arguments:
        
# environment -- is the raster environment to be shared with all agents.
# agents -- is a reference to all agents in environmet
# x -- is the x axis coordinate for this agent.
# y -- is the y axis coordinate for this agent.
    
    
# Defines the x and y property    
        
    def set_x(agentX, self):
        self.x = agentX
            
    def set_y (agentY, self): 
        self.y = agentY
   
# moves an agent in the x or y direction    
    def move(self):
        self.x = random.randint(0,100)        
        self.y = random.randint(0,100) 

            
# Agent eats/removes some of environemnt. 
             
    def eat(self): 
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
# If more than 10 get 10            
        else:
# Store what is left
            self.store += self.environment[self._y][self._x]
            self.environment[self._y][self._x] = 0
            
        #print(str(self.store))
        
        if self.store > 100:
            self.environment[self._y][self._x] = self.environment[self._y][self._x] + 50
            #print(str(self))
            self.store = 50
            #print(str(self))
            
# Agent shares some of environment with neighbours.
            
    def share_with_neighbours(self, neighbourhood):
        self.neighbourhood = neighbourhood
        
# Postional arguments:
# neighbourhood -- the proximity of agents in this Agent class
    
#print(neighbourhood)
        
        for agent in self.agents:
            if(self != agent):
                dist = self.distance_between(agent) 
                if dist <= neighbourhood:
                    sum = self.store + agent.store
                    ave = sum /2
                    self.store = ave
                    agent.store = ave
                    #print("sharing " + str(dist) + " " + str(ave))
       
# Calculates the distance between self and agent.
        
    def distance_between(self, agent):
        
# Postional arguments:
# agent -- an instance of this Agent class

# Returns:
# The distance between self and agent.
               
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
                
    