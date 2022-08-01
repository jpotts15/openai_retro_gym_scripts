import retro
import numpy as np
import cv2
import neat
import pickle
import gym


class Frameskip(gym.Wrapper):
    def __init__(self, env, skip=4):
        super().__init__(env)
        self._skip = skip

    def reset(self):
        return self.env.reset()

    def step(self, act):
        total_rew = 0.0
        done = None
        for i in range(self._skip):
            ob, rew, done, info = self.env.step(act)
            total_rew += rew
            if done:
                break

        return ob, rew, done, info


env = retro.make('BubbleBobble-Nes')
#env = Frameskip(env)

imgarray = []

def eval_genomes(genomes, config):


    for genome_id, genome in genomes:
        ob = env.reset()


        

        current_max_fitness = 0
        fitness_current = 0
        frame = 0
        counter = 0
        xpos = 0
        xpos_max = 0
        
        
        done = False
        
        while not done:
            ac = env.action_space.sample
        
            inx, iny, inc = env.observation_space.shape
            
            inx = int(inx/8)
            iny = int(iny/8)
            net = neat.nn.recurrent.RecurrentNetwork.create(genome, config) 
            blank = [0,0,0,0,0,0,0,0,0]
            env.render()
            frame += 1
            #scaledimg = cv2.cvtColor(ob, cv2.COLOR_BGR2RGB)
            #scaledimg = cv2.resize(scaledimg, (iny, inx)) 
            ob = cv2.resize(ob, (inx, iny))
            ob = cv2.cvtColor(ob, cv2.COLOR_BGR2GRAY)
            ob = np.reshape(ob, (inx,iny))
            #cv2.imshow('main', scaledimg)
            #cv2.waitKey(1) 

            imgarray = np.ndarray.flatten(ob)

            nnOutput = net.activate(imgarray)
            
            ##Normalize nnOutput to allow more functions to be used, retro only wants a 1 or 0 but many activations return floats
            print(nnOutput) 
            
            normalize = []
            
            for i in nnOutput:
                i = abs(i)
                if i >= 1:
                    a = round(1 // (i))
                    int(a)
                    normalize.append(a)
                else:
                    a = round(i)
                    int(a)
                    normalize.append(a)
                
            
            nnOutput.clear()
            nnOutput = normalize
            print(nnOutput) 
            rew_acc = 0
            ##Pad actions that don't matter
            #print(nnOutput) 
            nnOutput.insert(1,0)
            #print(nnOutput) 
            nnOutput.insert(1,0)
            #print(nnOutput)
            nnOutput.insert(1,0)
            #print(nnOutput)
            nnOutput.insert(1,0)
            #print(nnOutput)
            nnOutput.insert(1,0)
            #print(nnOutput)
            #ob, rew, done, info = env.step(blank)
            #rew_acc += int(rew)
            #ob, rew, done, info = env.step(blank)
            #rew_acc += int(rew)
            #ob, rew, done, info = env.step(blank)
            #rew_acc += int(rew)
            ob, rew, done, info = env.step(blank)
            rew_acc += rew  
            ob, rew, done, info = env.step(nnOutput)
            rew_acc += rew     
            ob, rew, done, info = env.step(blank)
            rew_acc += rew
            #ob, rew, done, info = env.step(blank)
            #rew_acc += int(rew)      
            #ob, rew, done, info = env.step(blank)
            #rew_acc += int(rew)
            #ob, rew, done, info = env.step(blank)
            #rew_acc += int(rew)
            #xpos = info['x']
            #xpos_end = info['screen_x_end']
            rew = (rew_acc//3)
            
            timetick = info['time_tick']
            
            #if xpos > xpos_max:
                #fitness_current += 1
                #xpos_max = xpos
            
            #if xpos == xpos_end and xpos > 500:
                #fitness_current += 100000
                #done = True
            
            fitness_current += rew
            
            if fitness_current > current_max_fitness:
                current_max_fitness = fitness_current
                counter -=200
            else:
                counter += 1
                
            if done or counter > 150:
                done = True
                print(genome_id, fitness_current)
                env.reset()
                
            #if done:
            #    if lives != 0:
            #        lives * -2000 -= fitness_current   
                #done = True
                #print(genome_id, fitness_current)
                #env.reset()
                
            genome.fitness = fitness_current

            
            #print(nnOutput)
            #print(stats)
        

config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                     neat.DefaultSpeciesSet, neat.DefaultStagnation,
                     'config-feedforward')

p = neat.Population(config)
#p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-1175')
p.add_reporter(neat.StdOutReporter(True))
stats = neat.StatisticsReporter()
p.add_reporter(stats)
p.add_reporter(neat.Checkpointer(10))

winner = p.run(eval_genomes)

with open('winner.pkl', 'wb') as output:
    pickle.dump(winner, output, 1)
