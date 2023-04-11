import retro
import numpy as np
import time

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

# Define the Q-learning parameters
learning_rate = 0.8
discount_factor = 0.95
num_episodes = 100

# Define the state and action spaces
num_states = 240*256*3
num_actions = 12

# Initialize the Q-table with zeros
q_table = np.zeros((num_states, num_actions))
np.load('q_table.npy')

# Create the environment
env = retro.make(game='BubbleBobble-Nes')

# Run the Q-learning algorithm for the specified number of episodes
for episode in range(num_episodes):
    # Reset the environment for a new episode
    state = env.reset()

    # Run the episode until termination
    done = False
    while not done:
        env.render()
        #print(q_table)
        # Choose the action with the highest Q-value for the current state
        if random.
        action = np.argmax(q_table[state])
        #print(action)
        action = int(action)
        action += 1

        if action > 0:
            if action ==  1:
                action1 = action_bubble
            if action ==  2:
                action1 = action_jump
            if action ==  3:
                action1 = action_right
            if action ==  4:
                action1 = action_left
            if action ==  5:
                action1 = action_down
            if action ==  6:
                action1 = action_up
            if action ==  7:
                action1 = action_jb
            if action ==  8:
                action1 = action_jbr
            if action ==  9:
                action1 = action_jbl
            if action ==  10:
                action1 = action_br
            if action ==  11:
                action1 = action_bl
            if action == 12:
                action1 = action_blank
        #print(action)
        #print(action1)
        action -= 1

        # Take the chosen action and observe the new state and reward
        next_state, reward, done, info = env.step(action1)
        # Update the Q-value for the current state-action pair
        q_table[state, action] += learning_rate * (reward + discount_factor * np.max(q_table[next_state]) - q_table[state, action])

        # Update the current state
        state = next_state.flatten().argmax()

        #add some frame skipping
        env.step(action_blank)
        env.step(action_blank)
        env.step(action_blank)
        env.step(action_blank)

    # Print the episode number and the total reward earned by the agent
    print("Episode: ", episode, " Total reward: ", info['score'])

    # Save the learned Q-table
    np.save('q_table.npy', q_table)

# Playback the learned policy
state = env.reset()
done = False
total_reward = 0
while not done:
    # Choose the action with the highest Q-value for the current state
    action = np.argmax(q_table[state])
    # print(action)
    action = int(action)
    action += 1

    if action > 0:
        if action == 1:
            action1 = action_bubble
        if action == 2:
            action1 = action_jump
        if action == 3:
            action1 = action_right
        if action == 4:
            action1 = action_left
        if action == 5:
            action1 = action_down
        if action == 6:
            action1 = action_up
        if action == 7:
            action1 = action_jb
        if action == 8:
            action1 = action_jbr
        if action == 9:
            action1 = action_jbl
        if action == 10:
            action1 = action_br
        if action == 11:
            action1 = action_bl
        if action == 12:
            action1 = action_blank
    # print(action)
    # print(action1)
    action -= 1

    # Take the chosen action and observe the new state and reward
    next_state, reward, done, info = env.step(action1)

    # Update the total reward
    total_reward += reward

    # Render the current state of the game
    env.render()

    # add some frame skipping
    env.step(action_blank)
    env.step(action_blank)
    env.step(action_blank)
    env.step(action_blank)

# Print the total reward earned by the agent
print("Total reward: ", total_reward)

# Close the environment
env.close()
