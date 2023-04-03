import retro
import numpy as np
import time

# Define the Q-learning parameters
learning_rate = 0.8
discount_factor = 0.95
num_episodes = 1000

# Define the state and action spaces
num_states = 240*256*3
num_actions = 9

# Initialize the Q-table with zeros
q_table = np.zeros((num_states, num_actions))

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
        # Choose the action with the highest Q-value for the current state
        action = np.argmax(q_table[state])

        # Take the chosen action and observe the new state and reward
        next_state, reward, done, info = env.step(np.array([action]))

        # Update the Q-value for the current state-action pair
        q_table[state, action] += learning_rate * (reward + discount_factor * np.max(q_table[next_state]) - q_table[state, action])

        # Update the current state
        state = next_state.flatten().argmax()

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

    # Take the chosen action and observe the new state and reward
    state, reward, done, info = env.step(np.array([action]))

    # Update the total reward
    total_reward += reward

    # Render the current state of the game
    env.render()

    # Wait a short amount of time to slow down the rendering
    time.sleep(0.01)

    # Print the current reward earned by the agent
    print("Current reward: ", info['score'])

# Print the total reward earned by the agent
print("Total reward: ", total_reward)

# Close the environment
env.close()
