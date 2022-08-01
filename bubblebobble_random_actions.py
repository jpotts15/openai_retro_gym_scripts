import random
import argparse
 
import numpy as np
import retro
import gym
import datetime


#Keymap
#define useful actions
action_blank =  [0,0,0,0,0,0,0,0,0]
action_bubble = [1,0,0,0,0,0,0,0,0]
action_jump =   [0,0,0,0,0,0,0,0,1]
action_right =  [0,0,0,0,0,0,0,1,0]
action_left =   [0,0,0,0,0,0,1,0,0]
action_down =   [0,0,0,0,0,1,0,0,0]
action_up =     [0,0,0,0,1,0,0,0,0]
action_jb =     [1,0,0,0,0,0,0,0,1]
action_jbr =    [1,0,0,0,0,0,0,1,1]
action_jbl =    [1,0,0,0,0,0,1,0,1]
action_br =     [1,0,0,0,0,0,1,0,0]
action_bl =     [1,0,0,0,0,0,0,1,0]



env = retro.make('BubbleBobble-Nes')

env.reset()

done = False


while not done:
    env.render()
    action = []
    #random action
    #acts = env.action_space.sample()
    #action.append(acts)

    #no action
    #action = [1,0,0,0,0,0,0,1,1]
    
    #input action
    #print('enter action')
    #action = input()
    for i in range(1):
    #    add random act
        #acts = env.action_space.sample()
        acts = env.action_space.sample()
        action.append(acts)     
        acts = action_blank
        action.append(acts)  

        
      
    
    #keymap usage
    for act in action:
        ob, rew, done, info = env.step(act)
        print(act)
        print("action", action)
        print("Image", ob.shape, "Reward", rew, "Done?", done)
        print("Info", info)
        if done is True:
            close = True
            env.render(close)
            env.reset()
            env.close()

#env.reset()
#env.close()