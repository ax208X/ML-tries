# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 15:22:15 2019

@author: Aisha.Xu
"""

import myenvironment
import json 

myenv = myenvironment.environment_easy21()
card = input('what is your card?')
dealer = input('what is the delears card?')
Q_type = input('which Q table you want to look up?Type 1 for the updated Qtable, 0 for the initial random Qtable. ')
card=card.split(',')
player = []
for items in card:
    player.append(int(items))
player = myenv.to_10_form(player)
player = myenv.to_update_form(player)
player.append(int(dealer))
print(player)
with open('Q_update1.json') as f:
    Q_update1 = json.load(f)

with open('Q_rad.json') as d:
    Q_rad = json.load(d)

if Q_type == '0':
    print(Q_rad[str(player)])
if Q_type == '1':
    print(Q_update1[str(player)])