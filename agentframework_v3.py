# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 11:00:17 2019

@author: 201289902
"""

import random
environment: list



class Agent():
    
    def set_x(agentX, self):
        self.x = agentX
            
    def set_y (agentY, self): 
        self.y = agentY
          
        
    def move(self):
        self.x = random.randint(0,100)        
        self.y = random.randint(0,100)
    
        
    def eat(self): 
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
        
    def share_with_neighbours(self, neighbourhood):
        self.neighbourhood = neighbourhood
        
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
                
    def get_x(self):
#####            return self.x      
        def get_y(self):
    #            return self.y
            def get_z(self):
    #            return self.z                    
                def __init__(self, environment):
#####     
                    if (x == None):
                            self.x = random.randint(0,100)
                    else:
                        self._x = x
                            
                            
                    if (y == None):
                            self.y = random.randint(0,100)
                    else:
                        self._y = y
                            
                            
                    if (z == None):
                            self.z = random.randint(0,100)
                    else:
                        self._z = random.randint(0,100)
     
        def __init__(self, environment): 
           self.environment = environment
           self.store = 0
#    

    
#    def distance_between(agents_row_a, agents_row_b):
#        return (((agents_row_a.x - agents_row_b.x)**2) +
#    ((agents_row_a.y - agents_row_b.y)**2))**0.5
                

#
     