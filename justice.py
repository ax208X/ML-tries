# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 13:38:42 2019

@author: Aisha.Xu
"""
"""This is the algorithm to justice win, lose and not-finished-yet"""
class rule():
    def __init__(self,x,y,position_storage):
        self.x = x
        self.y = y
        self.position_storage = position_storage

    def position_to_str(self,x,y):
        return str(x)+','+str(y)        
    
    
    
    def justice(self):
        position_storage = self.position_storage
        x = self.x
        y = self.y
        terminate = False
        value = position_storage[self.position_to_str(x,y)]
        #print(value)
        
        
        #check vertically
        #print('vertically')
        sum_ = 0
        chance = 0
        y_d = y
        x_d = x
        
        while (abs(sum_)<5) and (chance <2):
            if self.position_to_str(x_d,y_d) in position_storage.keys():
                k = position_storage[self.position_to_str(x_d,y_d)]
                #print(k)
                if k == value:
                    sum_ += k
                    if chance == 0:
                        y_d += 40
                    else:
                        y_d -= 40
                else:
                    chance +=1
                    y_d = y
                    x_d = x
                    y_d -= 40
                #print(chance)
            else:
                chance +=1
                y_d = y
                x_d = x
                y_d -= 40
                #print(chance)
            
        if sum_ == 5:
            result = 'Black wins!'
            terminate = True
        if sum_ == -5:
            result = 'Pink wins!'
            terminate = True
        
        #check horizontally
        if terminate == False:
            #print('horizontally')
            sum_ = 0
            chance = 0
            y_d = y
            x_d = x
            while (abs(sum_)<5) and (chance <2):
                if self.position_to_str(x_d,y_d) in position_storage.keys():
                    k = position_storage[self.position_to_str(x_d,y_d)]
                    #print(k)
                    if k == value:
                        sum_ += k
                        #print('sum=',sum_)
                        if chance == 0:
                            x_d += 40
                        else:
                            x_d -= 40
                    else:
                        chance +=1
                        y_d = y
                        x_d = x
                        x_d -= 40
                        #print(chance)
                else:
                    chance +=1
                    y_d = y
                    x_d = x
                    x_d -= 40
                    #print(chance)
            
            if sum_ == 5:
                result = 'Black wins!'
                terminate = True
            if sum_ == -5:
                result = 'Pink wins!'
                terminate = True
        
        #check diagonally:leftup to rightdown
        
        if terminate == False:
            #print('diagonally:leftup to rightdown')
            sum_ = 0
            chance = 0
            y_d = y
            x_d = x
            while (abs(sum_)<5) and (chance <2):
                if self.position_to_str(x_d,y_d) in position_storage.keys():
                    k = position_storage[self.position_to_str(x_d,y_d)]
                    #print(k)
                    if k == value:
                        sum_ += k
                        if chance == 0:
                            x_d += 40
                            y_d += 40
                        else:
                            x_d -= 40
                            y_d -= 40
                    else:
                        chance +=1
                        y_d = y
                        x_d = x
                        x_d -= 40
                        y_d -= 40
                        #print('chance=',chance)
                    #print(x_d,y_d)
                else:
                    chance +=1
                    y_d = y
                    x_d = x
                    x_d -= 40
                    y_d -= 40
                    #print('chance=',chance)
                    #print(x_d,y_d)
             
            if sum_ == 5:
                result = 'Black wins!'
                terminate = True
            if sum_ == -5:
                result = 'Pink wins!'
                terminate = True
        
        #check diagonally:leftdown to rightup
        
        if terminate == False:
            #print('diagonally:leftdown to rightup')
            sum_ = 0
            chance = 0
            y_d = y
            x_d = x
            while (abs(sum_)<5) and (chance <2):
                if self.position_to_str(x_d,y_d) in position_storage.keys():
                    k = position_storage[self.position_to_str(x_d,y_d)]
                    #print(k)
                    if k == value:
                        sum_ += k
                        if chance == 0:
                            x_d += 40
                            y_d -= 40
                        else:
                            x_d -= 40
                            y_d += 40
                    else:
                        chance +=1
                        y_d = y
                        x_d = x
                        x_d -= 40
                        y_d += 40
                        #print('chance=',chance)
                    #print(x_d,y_d)
                else:
                    chance +=1
                    y_d = y
                    x_d = x
                    x_d -= 40
                    y_d += 40
                    #print('chance=',chance)
                    #print(x_d,y_d)
             
            if sum_ == 5:
                result = 'Black wins!'
                terminate = True
            if sum_ == -5:
                result = 'Pink wins!'
                terminate = True
        
        
        if terminate == False:
            result = False
        return result

#position = {'200,240': -1, '240,280': 1, '240,200': -1, '280,240': 1, '280,280': -1, '320,200': 1, '360,240': -1, '360,160': 1, '400,200': -1, '400,120': 1}
#x = 400
#y = 120
#j = rule(x,y,position)
#print(j.justice())