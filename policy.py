# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 13:58:10 2019

@author: Aisha.Xu
"""

import reju_RL as rej
import numpy as np
import justice
import random

model = rej.TDmodel()
class policy():
    def __init__(self,theta):
        self.theta = theta
        self.board = np.zeros((17,17),dtype = int)
    
    def position2board(self,position):
        board = self.board
        for keys in position:
            #print(type(keys))
            x,y=model.str_to_position(keys)
            i = int((x/40)-1)
            j = int((y/40)-1)
            #print(i,j)
            #print(position[keys])
            board[i][j]=int(position[keys])
        return board
    
    def move(self,theta,position_storage):
        q=0
        
        board_global = self.position2board(position_storage)
        #position_global = position_storage
        #print(board_global)
        avail_p = np.where(board_global==0)
        #print('avail_p',avail_p)
        #board_str = str(board.reshape(-1))
        #board = board.reshape(17,17)
        #print('reward=0,1',board,board.shape)
        #position = self.store_board(board)
        for i,j in zip(avail_p[0],avail_p[1]):
            print(board_global)
            board = self.position2board(position_storage)
            position = position_storage
            print('global',board_global,position_storage, position)
            action = [i,j]
            board[i][j]=-1
            board_new = board
            position_new = model.store_position(board_new,position,i,j)
            print('new position',position_new)
            x = (i+1)*40
            y = (j+1)*40
            j = justice.rule(x,y,position_new)
            result = j.justice() 
            if result == 'Pink wins!':
                move = [x,y]
                q = 1
                break
        
            board = board.reshape(-1)
            board_action = list(board)
            board_action.append(action[0])
            board_action.append(action[1])
            board_action = np.array(board_action)
            q_board = sum(board_action * theta)
            print(q_board)
            if q_board > q:
                q = q_board
                move = [x,y]
                
        #epsilon-greedy policy
        decide = random.choices(population = [0,1],weights = [1-abs(q),abs(q)])
        board = board_global
        if decide == 0:
            position_fine = False
            while (position_fine == False):
                i = random.choice(range(17))
                j = random.choice(range(17))
                if board[i][j] == 0:
                    position_fine = True
             
            x = (i+1)*40
            y = (j+1)*40
            move = [x,y]
            
        return q, move
        
