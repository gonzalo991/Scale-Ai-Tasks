/**
High Level: ML/AI

Category:
Deep Learning

Topic:
Reinforcement Learning

Operation for 1st prompt (you only need to follow this for your 1st prompt):

Rewrite: Ask the assistant to edit or modify an existing piece of code following various instructions.
 */

/**
 * 1. improve this code adding reward shaping
// Define the Gridworld environment
const gridWorld = [
[0, 0, 0, 0],
[0, -1, 0, -1],
[0, 0, 0, 0],
[-1, 0, 0, 1]
];

// Initialize Q-table
const qTable = [
[0, 0, 0, 0],
[0, 0, 0, 0],
[0, 0, 0, 0],
[0, 0, 0, 0]
];

// Set hyperparameters
const learningRate = 0.1;
const discountFactor = 0.9;
const epsilon = 0.1;

// Define the possible actions
const actions = [‘up’, ‘down’, ‘left’, ‘right’];

// Function to choose an action based on Q-values
function chooseAction(state) {
if (Math.random() < epsilon) {
// Exploration: choose a random action
return actions[Math.floor(Math.random() * actions.length)];
} else {
// Exploitation: choose the action with the highest Q-value
const qValues = qTable[state];
const maxQValue = Math.max(…qValues);
const maxQIndices = qValues.reduce(
(acc, qValue, index) => (qValue === maxQValue ? […acc, index] : acc),
[]
);
return actions[maxQIndices[Math.floor(Math.random() * maxQIndices.length)]];
}
}

// Function to update the Q-table based on the action and resulting state
function updateQTable(state, action, nextState, reward) {
const qValue = qTable[state][actions.indexOf(action)];
const maxNextQValue = Math.max(…qTable[nextState]);
const updatedQValue = qValue + learningRate * (reward + discountFactor * maxNextQValue - qValue);
qTable[state][actions.indexOf(action)] = updatedQValue;
}

// Function to run the Q-learning algorithm
function trainQLearning(episodes) {
for (let episode = 0; episode < episodes; episode++) {
let state = 0; // Starting state
let steps = 0;

while (state !== 15) {
  const action = chooseAction(state);

  let nextState, reward;
  if (action === 'up' && state >= 4) {
    nextState = state - 4;
    reward = gridWorld[Math.floor(state / 4) - 1][state % 4];
  } else if (action === 'down' && state <= 11) {
    nextState = state + 4;
    reward = gridWorld[Math.floor(state / 4) + 1][state % 4];
  } else if (action === 'left' && state % 4 !== 0) {
    nextState = state - 1;
    reward = gridWorld[Math.floor(state / 4)][state % 4 - 1];
  } else if (action === 'right' && state % 4 !== 3) {
    nextState = state + 1;
    reward = gridWorld[Math.floor(state / 4)][state % 4 + 1];
  } else {
    nextState = state;
    reward = -1; // Penalty for invalid actions
  }

  updateQTable(state, action, nextState, reward);

  state = nextState
  }
}
 */

/**
The code you provided is a basic implementation of the
 Q-learning algorithm with a GridWorld environment. I have 
 added reward shaping to the updateQTable function:
 */
// Define the Gridworld environment
const gridWorld = [
    [0, 0, 0, 0],
    [0, -1, 0, -1],
    [0, 0, 0, 0],
    [-1, 0, 0, 1]
];

// Initialize Q-table
const qTable = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
];

// Set hyperparameters
const learningRate = 0.1;
const discountFactor = 0.9;
const epsilon = 0.1;

// Define the possible actions
const actions = ['up', 'down', 'left', 'right'];

// Function to choose an action based on Q-values
function chooseAction(state) {
    if (Math.random() < epsilon) {
        // Exploration: choose a random action
        return actions[Math.floor(Math.random() * actions.length)];
    } else {
        // Exploitation: choose the action with the highest Q-value
        const qValues = qTable[state];
        const maxQValue = Math.max(...qValues);
        const maxQIndices = qValues.reduce(
            (acc, qValue, index) => (qValue === maxQValue ? [...acc, index] : acc),
            []
        );
        return actions[maxQIndices[Math.floor(Math.random() * maxQIndices.length)]];
    }
}

// Function to update the Q-table based on the action and resulting state
function updateQTable(state, action, nextState, reward) {
    const qValue = qTable[state][actions.indexOf(action)];

    // Reward shaping
    const shapedReward = reward + 10; // Add a bonus to all rewards

    const maxNextQValue = Math.max(...qTable[nextState]);
    const updatedQValue = qValue + learningRate * (shapedReward + discountFactor * maxNextQValue - qValue);
    qTable[state][actions.indexOf(action)] = updatedQValue;
}

// Function to run the Q-learning algorithm
function trainQLearning(episodes) {
    for (let episode = 0; episode < episodes; episode++) {
        let state = 0; // Starting state
        let steps = 0;

        while (state !== 15) {
            const action = chooseAction(state);

            let nextState, reward;
            if (action === 'up' && state >= 4) {
                nextState = state - 4;
                reward = gridWorld[Math.floor(state / 4) - 1][state % 4];
            } else if (action === 'down' && state <= 11) {
                nextState = state + 4;
                reward = gridWorld[Math.floor(state / 4) + 1][state % 4];
            } else if (action === 'left' && state % 4 !== 0) {
                nextState = state - 1;
                reward = gridWorld[Math.floor(state / 4)][state % 4 - 1];
            } else if (action === 'right' && state % 4 !== 3) {
                nextState = state + 1;
                reward = gridWorld[Math.floor(state / 4)][state % 4 + 1];
            } else {
                nextState = state;
                reward = -1; // Penalty for invalid actions
            }

            updateQTable(state, action, nextState, reward);

            state = nextState;
            steps++;
        }
    }
}

// Usage
trainQLearning(1000);
/**
The updateQTable function is modified to add reward shaping in this updated code.
This effectively shapes the rewards to encourage faster learning and convergence by
adding a bonus of 10 to all rewards. Depending on your specific needs and the impact you
want to have on the learning process, you can adjust the value of the bonus.
 */

// 2. What is the purpose of the `qTable` variable in the code?

/** The qTable variable is a 2D array used to store the Q-values of the Q-learning algorithm.The 
Q-values represent the quality or "goodness" of a state.

The qTable[state] array holds the Q-values for a particular state. The actions parameter
contains the possible actions. The qTable[state][actions.indexOf(action)] holds the Q-value
for a particular action in a state.

Overall, the qTable variable represents the Q-table, a data structure used to store Q-values
for each state-action pair in the reinforcement learning algorithm. Each row represents one condition
and each column represents one action. The values in the table represent the expected return or the
expected utility of performing a particular action in a particular state. The Q-values are updated
during the training process on the basis of the agent's interactions with the environment, and they
guide the agent's decision-making process by determining the best action to take in each state. */




// 3. How is the action chosen in the chooseAction function? Explain the exploration-exploitation trade-off in this code



/**The action is chosen in the chooseAction function using a combination of exploration and exploitation. 
The function first uses a random number generator to select an action with a probability of epsilon. 
This ensures that the agent explores new actions and doesn't get stuck in a local optimum. With the 
remaining probability, the function chooses an action that maximizes the expected return, or the expected 
utility, of the action. This ensures that the agent exploits the best action available in a given state.

The first thing the function does is to check whether a randomly generated number is smaller than 
the exploration rate (epsilon). If this is the case, then the function will select a random action 
from the list of possible actions. Choosing a random action encourages exploration, allowing the agent 
to try different actions and learn how they affect the environment.

However, the function will choose the action with the highest Q-value for the current state if the random 
number is greater than or equal to epsilon. This is the exploitation part of the trade-off. Exploitation is 
the selection of the action that is expected to yield the highest future reward on the basis of the learned
Q-values. The exploitation of Q-values is the agent's attempt to make optimal decisions and maximise its 
long-term cumulative reward.

The exploration-exploitation trade-off is a key concept in reinforcement learning. It is the balance 
between exploring new actions and exploiting the best action available. A high value of epsilon will 
encourage exploration, while a low value will encourage exploitation. The trade-off is important because 
it allows the agent to explore new actions and learn about the environment, while also exploiting the best 
action available to maximize the expected return.

The choice of action in the chooseAction function is based on this exploration-exploitation trade-off. 
The function first uses a random number generator to select an action with a probability of epsilon. 
This ensures that the agent explores new actions and doesn't get stuck in a local optimum. With the remaining 
probability, the function chooses an action that maximizes the expected return, or the expected utility, 
of the action. This ensures that the agent exploits the best action available in a given state. */



// 4. How is the Q-table updated in the updateQTable function in this code? What is the significance 
// of the learning rate and discount factor shown above?



/**In the updateQTable function, the Q-table is updated on the basis of the action taken, 
the resulting state, the reward received and the maximum Q-value of the next state.

The function first obtains the current score for the given state and action from the score table. 
Then, by taking the maximum value among the Q-values corresponding to the possible actions in the 
next state, it calculates the maximum Q-value for the next state.

The update equation that is used to update the Q value in the Q table is as follows:

```javascript
updatedQValue = qValue + learningRate * (reward + discountFactor * maxNextQValue - qValue)
```

In reinforcement learning, the trade-off between exploration and exploitation refers to the 
balance between the exploration of new actions and the exploitation of current knowledge to 
maximise the reward. While learning, the agent needs to explore different actions to discover 
potentially better strategies, while also using the learned knowledge to make optimal decisions 
based on the current information.

This trade-off is implemented using an epsilon-greedy policy in the chooseAction function. 
With probability epsilon, the agent explores by randomly choosing one of the available actions, 
which allows exploring different states and actions. With a probability of 1 - epsilon, the agent 
exploits the current knowledge by choosing the action with the highest Q-value. Q-value is a measure 
of the expected future rewards for a given state-action pair.

The influence of new information on updating Q-values is determined by the learning rate. 
A higher learning rate means that the agent gives more weight to the newly observed reward and 
makes a larger adjustment to the Q-values. In the early stages of learning, when the agent needs to 
adapt quickly to new information, this can be beneficial. However, a high learning rate can also lead 
to instability or overfitting if it is too high. Often, you will need to experiment with different learning 
rates and observe the effects on the agents' learning progress and stability.

The discount factor (discountFactor) determines the importance of the future rewards in comparison 
to the immediate rewards. A value closer to 1 means that the agent places a higher value on long-term 
rewards and is more patient in the accumulation of rewards over time. On the other hand, a value closer 
to 0 means that immediate rewards are given more weight and that the agent is more focused on immediate gains. 
Choosing the discount factor depends on the specific problem and the trade-off between short and long term rewards. For example, a lower discount factor may be preferred in scenarios where immediate rewards are critical. Similarly, in tasks involving delayed rewards, a higher discounting factor may encourage the agent to plan for the long term.

It is an empirical process, often requiring experimentation and iterative adjustments, 
to fine-tune the learning rate and discount factor. It is common practice to start with a moderate 
learning rate and discount factor, and to observe the progress of the agent's learning. The learning 
rate can be increased to give more weight to new information if the agent's learning is slow or unstable. 
The discount factor can be adjusted if the agent focuses too much on immediate rewards or fails to consider 
long-term consequences. To find the optimal combination of hyperparameters for a given problem, it is 
important to monitor the agent's performance, observe convergence, and analyse the balance between exploration 
and exploitation.

In addition, techniques can be used to systematically explore the hyperparameter space and find the optimal
values, such as grid search, random search, or more advanced optimisation algorithms. Reinforcement learning 
is a complex area, and finding the right hyper-parameters is often a process of trial and error, coupled with 
domain expertise and a good understanding of the problem at hand.

Keep in mind that the effectiveness of the reinforcement learning agent depends not only on the learning
rate and the discount factor, but also on other factors such as the state representation, the reward design,
the exploration strategy, and the complexity of the environment. To improve the performance of the agent, 
it is important to consider these factors together and to iteratively refine the learning process. */

// 5. In this code what is the purpose of the trainQLearning function? How many episodes does it run for?

/** The `trainQLearning` function is used to train the Q-learning agent. It runs for a specified 
number of episodes, as defined by the user.

The function first initializes the state to 0. Then, it chooses an action for the current state 
based on the exploration-exploitation trade-off. The function then updates the Q-table based on 
the chosen action, the resulting state, and the reward received. This process is repeated until the 
agent has converged to an optimal policy or until the specified number of episodes has been reached.

The number of episodes is a hyperparameter that can be set by the user. The choice of the number of 
episodes depends on the problem complexity and the desired level of convergence. In general, the more 
complex the problem, the more episodes may be needed to converge to an optimal policy.

Here is a step-by-step explanation of the Q-learning algorithm that is implemented in the code provided:
1. Definition of the gridworld environment — The code starts with the definition of the Gridworld environment, 
which is represented by a 2D array (gridWorld). Each cell in the array represents a state. The values in the 
cells represent the rewards associated with each state.
2. Initialisation of the Q-table — The Q-table (qTable) is initialised as a 2D array in which all the values 
are set to zero. For each state-action pair, the Q-table stores the estimated future rewards (Q-values).
3. Hyper-parameter tuning — Hyperparameters such as the learning rate (learningRate), the discount factor 
(discountFactor) and the exploration rate (epsilon) are defined. The learning process and the trade-off 
between exploration and exploitation are controlled by these hyperparameters.
4. Definition of possible actions — An array (actions) of possible actions that the agent can take in 
each state is defined.
5. Use the epsilon greedy policy to choose an action — The chooseAction function is responsible for the 
selection of an action for the agent. In order to balance exploration and exploitation, it uses an 
epsilon-greedy policy. With probability epsilon a random action is chosen to explore and with probability 
(1 - epsilon) the action with the highest Q is chosen to exploit.
6. The Q table is updated — After choosing an action, the agent interacts with the environment. 
It observes the next state and the reward associated with the action. To update the Q-value in the 
Q-table for the current state-action pair, the updateQTable function is called. The Q is updated using 
the Q-learning equation, which considers the observed payoff, the maximum Q of the next state, 
the learning rate, and the discount rate.
7. Repeat steps 5 and 6 until the final state is reached — The agent continues to select actions, 
update the Q-table, and transition to the next state based on the selected action. This process 
continues until the agent reaches the terminal state, which in this code is when state 15 is reached.
8. Repetition for several episodes — The trainQLearning function wraps the above steps in a loop. 
The loop runs for the specified number of episodes. Each episode allows the agent to gain experience, 
to learn from the rewards and to update the Q-values. Through repetition of this process, the agent can 
improve its decision making abilities and converge to optimal action policies.

It's important to note that the number of episodes is just one of many hyperparameters that can be 
tuned to improve the performance of the agent. The choice of the learning rate, the discount factor, 
and other hyperparameters can also have a significant impact on the agent's performance. */