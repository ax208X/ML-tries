# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 14:14:11 2019

@author: Aisha.Xu
"""

#import numpy as np
import myenvironment as myenv
#import random
import policy
import MC_21_control

game = myenv.environment_easy21()
pi = policy.policies(None)
MC = MC_21_control.MCmodel()

Q_rad = MC.rad_train(200)
Q = Q_rad
n = 10

for i in range(n):
    Q = MC.further_train(200,Q)
    print(Q)

Q_update1 = Q
print('Q_rad=',Q_rad)
print('Q_update1 =',Q_update1)

import json

with open('Q_rad.json', 'w') as f:
    json.dump(Q_rad, f)

# elsewhere...
with open('Q_update1.json', 'w') as f:
    json.dump(Q_update1, f)