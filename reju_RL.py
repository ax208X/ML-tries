# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 14:30:21 2019

@author: Aisha.Xu
"""
"""This is the reinforcement learning algorithm, use linear combination model. I also include a function of
generating training sets. A tedious thing is I used two ways to store the board state- one is a 17*17 array,
and the other is a position_storage dictionary, storing the location coordinates(in the canvas, so there is a 
*40 things) and -1 for pink or 1 for black"""

import numpy as np
import random
import justice
from matplotlib.pyplot import *
"""pink is the computer,pink is -1"""


class TDmodel(object):
    def __init__(self):
        theta = np.random.randn(17*17+2)/np.sqrt(17*17+2)
        self.theta = theta #np.reshape(theta,(17,17))
        self.board = np.zeros((17,17),dtype = int)
    
    #turn a position coordinate into string
    def position_to_str(self,x,y):
        return str(x)+','+str(y)
    #turn a string into coordinate form
    def str_to_position(self,p):
        p = p.split(',')
        x = int(p[0])
        y = int(p[1])
        return x,y
    
    #store a board in position_storage dictionary form
    def store_board(self,board):
        position_storage = {}
        for i in range(17):
            for j in range(17):
                x = (i+1)*40
                y = (j+1)*40
                position_storage[self.position_to_str(x,y)] = board[i][j]
        return position_storage
    
    #store a position in position_storage dictionary
    def store_position(self,board,position,i,j):
        x = (i+1)*40
        y = (j+1)*40
        position[self.position_to_str(x,y)] = board[i][j]
        return position
         
                  
    def train_set(self,size):
        trainset = {}
        for n in range(size):
            s = 1
            board = np.zeros((17,17),dtype = int)
            position_storage = self.store_board(board)
            step = random.choice(range(334))+1
            if step%2 == 0:
                step += 1
            k = 1
            terminate = False
            reward = 0
            while k <= step and terminate == False:
                position_fine = False
                while (position_fine == False):
                    i = random.choice(range(17))
                    j = random.choice(range(17))
                    if board[i][j] == 0:
                        board[i][j] = s
                        position_fine = True
                         #print('ok',position_fine)
                 #print('out')
                position_storage = self.store_position(board,position_storage,i,j)
                j = justice.rule((i+1)*40,(j+1)*40,position_storage)  
                result = j.justice()
                if result == 'Pink wins!':
                    reward = 1
                    terminate = True
                if result == 'Black wins!':
                    reward == -1
                    terminate = True
                   
                if s == 1:
                    s = -1
                else:
                    s = 1
                k += 1
                 #k is odd:black's turn(player),k is even:pink's turn(computer)
             
            board_str = str(board.reshape(-1))
            board = board.reshape(17,17)
        
            trainset[board_str]={'positions':position_storage,'reward':reward,'board':board,'step':k}
        return trainset
     
    def qhat_storage(self,theta,board,action,q_storage):
        q = q_storage   
        board = board.reshape(-1)
        board_action = list(board)
        board_action.append(action[0])
        board_action.append(action[1])
        board_action = np.array(board_action)
        q_board = board_action * theta
        #print(q_board)
        q[str(board)]={'action':action,'q_approx':sum(q_board)}
        return q

    def grad_J(self,qhat,q_dict):
        cha = np.zeros(17*17+2)
        for key in q_dict.keys():
            board = q_dict[key]['board']
            action = q_dict[key]['action']
            board = board.reshape(-1)
            board = list(board)
            board.append(action[0])
            board.append(action[1])
            board_action = np.array(board)
            #print('Q=',q_dict[key]['Q'])
            #print('qhat=',qhat[key]['q_approx'])
            cha += (q_dict[key]['Q']-qhat[key]['q_approx'])*board_action
        cha = cha/len(q_dict.keys())
        return cha
    
    def cal_MSE(self,qhat,Q):
        MSE = 0
        for key in Q.keys():
            MSE += (qhat[key]['q_approx']-Q[key]['Q'])**2
        MSE = MSE/len(Q.keys())
        return MSE
    
    def tdtrain(self,trainset,theta,gamma):
        Q = {}
        qhat = {}
        #print('length=',len(trainset.keys()))
        for keys in trainset:
            #print(keys)
            state = trainset[keys]
            board = state['board']
            #print(board,type(board))
            reward = state['reward']
            #print('reward=',reward)
            position_storage = state['positions']
            step = state['step']
            if reward > 0:
                winning_p = np.where(board==-1)
                for i,j in zip(winning_p[0],winning_p[1]):
                    #print(board,type(board))
                    board[i][j] = 0
                    board_str = str(board.reshape(-1))
                    board = board.reshape(17,17)
                    position = self.store_board(board)
                    action = [i,j]
                    Q[board_str] = {'positions':position_storage,'Q':reward,'board':board,'action':action}
                    qhat = self.qhat_storage(theta,board,action,qhat)
            if reward < 0:
                losing_p = np.where(board==-1)
                black_p = np.where(board==1)
                for i,j in zip(losing_p[0],losing_p[1]):
                    #print('reward<0,1',board,type(board))
                    board[i][j] = 0
                    for ib,jb in zip(black_p[0].black_p[1]):
                        board[i1][j1]=0
                        board_str = str(board.reshape(-1))
                        board = board.reshape(17,17)
                        position = self.store_board(board)
                        action = [i,j]
                        Q[board_str] = {'positions':position_storage,'Q':reward,'board':board,'action':action}
                        qhat = self.qhat_storage(theta,board,action,qhat)
            if reward == 0:
                avail_p = np.where(board==0)
                board_str = str(state['board'].reshape(-1))
                board = board.reshape(17,17)
                #print('reward=0,1',board,board.shape)
                position = self.store_board(board)
                for i,j in zip(avail_p[0],avail_p[1]):
                    board = state['board']
                    #print('reward=0,2',board,board.shape)
                    action = [i,j]
                    qhat = self.qhat_storage(theta,state['board'],action,qhat)
                    board = board.reshape(17,17)
                    #print('reward=0,3',board,board.shape)
                    board[i][j]=-1
                    position_storage = self.store_board(board)
                    j = justice.rule((i+1)*40,(j+1)*40,position_storage)  
                    result = j.justice()
                    if result ==False:
                        reward = 0
                        board = board.reshape(-1)
                        board = list(board)
                        board.append(action[0])
                        board.append(action[1])
                        board = np.array(board)
                        q_board = board * theta
                        Q[board_str]={'positions':position,'Q':gamma*sum(q_board),'board':state['board'],'action':action}
                    elif result == 'Black wins!':
                        reward = -1
                        Q[board_str]={'positions':position,'Q':reward,'board':state['board'],'action':action}
                    elif result == 'Pink wins!':
                        reward == 1
                        Q[board_str]={'positions':position,'Q':reward,'board':state['board'],'action':action}
    
        cha = self.grad_J(qhat,Q)
        train_size = len(trainset.keys())
        #print(cha)
        print(1/100000*np.sqrt(17*17+2))
        theta = np.array(theta)+(1/10000*np.sqrt(17*17+2))*(cha)
        return theta,Q,qhat
    
    def tdepoch(self,epoch,size):
        theta = self.theta
        print('theta=',theta)
        MSE_list = []
        count = list(range(epoch))
        for n in range(epoch):
            print('n=',n)
            trainset = self.train_set(size)
            theta,Q,qhat = self.tdtrain(trainset,theta,1)
            print('theta=',theta)
            MSE = self.cal_MSE(qhat,Q)
            print('MSE=',MSE)
            MSE_list.append(MSE)
        return theta,count,MSE_list
    

#model = TDmodel()
#theta,count,MSE_list = model.tdepoch(20,300)
#plot(count,MSE_list)
#show()

            
                    
            
            
                   
                    
            
