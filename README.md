# openai_retro_gym_scripts
Some OpenAI Retrogym scripts and related 

Most of this is derived from: 
openai gym retro - https://retro.readthedocs.io/en/latest/index.html

Lucas Thompson - Results of Tutorial on Sonic 2 - EP0 - Open-AI and NEAT Tutorial - https://www.youtube.com/watch?v=pClGmU1JEsM&list=PLTWFMbPFsvz3CeozHfeuJIXWAJMkPtAdS&index=1&t=7s

deepanshut041 - Reinforcement-Learning, Implementations of Deep Reinforcement Learning Algorithms and Bench-marking with PyTorch - https://deepanshut041.github.io/Reinforcement-Learning/cgames/05_sonic/

tom7 - Computer program that learns to play classic NES games - https://www.youtube.com/watch?v=xOCurBYI_gY

AI Playpen - Can AI learn to play [Bubble Bobble]? (NES) - https://www.youtube.com/watch?v=srWLzDyfM8M

My Videos:
Video Example - https://youtu.be/FbtvmHh47L4

Overview:
Original inspriation to try building a retro gameplaying AI was from the Tom7 video above but quickly found the openai gym retro which takes care of most of the work and makes this something that anyone with basic python, linux, etc experience can do. 

I found that most of these gameplaying AIs are built for side scrollers so I wanted to try on a less straight forward game. In side scrollers the main method I've seen is rewarding moving in the correct direction while avoiding enemies. I choose bubble bobble as it was something I played a lot when I was younger but it also fits well as it has:
1. Each level is unique
2. Progression requires killing all enemies on each level 
3. Enemies vary and don't always behave the same
4. Rewards are somewhat delayed or require sets of actions

Goal:
Build a AI that can beat Bubble Bobble

Requirements:
1. Keep the AI general so that it can play other games or be modified to act on other combinations of other inputs/outputs
2. Create reproducable results
3. Use a machine learning untrained reinforcement AI
4. Display the screen as the AI plays

State:
Unfinished, all AIs so far have hit a wall at one place or another. This is a side project so updating as I have time and inclination. 

Observations:
1. Most AI algos perform similarly 
2. A random bot (one that just creates a list of random actions and does them) performs well mainly due to the speed it can brute force actions that create rewards
3. Most AIs get stuck in a looping action that beats early levels but gets stuck later on
4. One commonly used technique is to limit the number of actions/steps the game can play to ensure the AI isn't sitting idle. I've found its better to cap the unrewarded steps instead of using an absolute value as some functions generate tail end activity which helps with changing/evolving actions
5. Bubble bobble allows for input faster then action can take place so padding is added so that only real actions are computed

Improvements Implemented:
1. Normalized the output of the neural network (hidden and direct outputs) 
	The retro gym wants list output for the action containing 9 values for NES. It will accept float values in the list but only seems to act on a 1 and everything else is considered a zero (although need to confirm in code). Normalizing this creates a wider range of actions closer to what the AI wants. Also negative values and values out of bound cause crashing.
	Originally only a few of the hidden node types were avaliable due to these limitations but normalizing allows for all to be used.
2. Pickle the neural network state 
3. Looped through random levels to arbitary train good actions instead of deterministic actions
4. Hashing of the screen to give a different way to feed inputs into the network

Improvements needed: 
1. Better evolution/randomization later to break out of loops
2. Better optimization
3. Improve parallelization, can be run currently but not displaying the screen 

Quick overview to build the enviorment:
1. Install python 3.8
2. Build a new virtual enviroment for retro gym
3. Follow the getting started on the Gym Retro readthedocs page
4. (optional) Install neat-python if using that as the AI framework
5. Follow the importing ROMs section to import bubblebobble-nes
6. Load the scenario and data jsons into the bubblebobble-nes folder
7. Run the desired script

To Do:
1. Import all AI scripts
2. Move the normilization into a module
3. Branch from the proper repos, openai retro gym is archived but a few others have active gits for it
