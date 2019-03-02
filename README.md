# Markov-Decision-Process
Solving MDP, read README for details

Solve the following MDP using both value iteration and policy iteration, you can do this by hand or programmatically, but you need to show your work in either case.

There is a self-driving taxi that takes from place to place. Its goal is to make the most money possible and it makes the most money in a particular town, MoneyTown. The taxi has a tendency to take routes that take it to different towns and it costs money for the taxi to drive from place to place.

There are three states that the taxi can be in: 'In MoneyTown', 'MoneyTown Suburbs', and 'Outside MoneyTown'. There are two actions that the taxi can take in each state: drive and wait. Driving costs \$10. When the taxi is in money town it makes \$30, in MoneyTown Suburbs and Outside MoneyTown it only makes \$10. The reward for the taxi is:

(money made - cost)

For example if the taxi is driving around in MoneyTown, the reward is \$30-\$10=\$20.

If the taxi is in MoneyTown and drives, then it is still MoneyTown in the next period with probability .9, and in the MoneyTown Suburbs in the next period with probability .1. If it is MoneyTown and does not drive, these probabilities are .7 and .3, respectively. If it is in the MoneyTown Suburbs and drives, then with probability .3 it is in MoneyTown in the next period, with probability .6 it is still in MoneyTown Suburbs in the next period, and with probability .1 it is in Outside MoneyTown in the next period. If it is in MoneyTown Suburbs and does not drive, then with probability 1 it is Outside MoneyTown next period. Finally, if it is in Outside MoneyTown and drives, then in the next period it is in MoneyTown with probability .6, and at the OutSide MoneyTown with probability .4. If it does not drive, then with probability 1 it is at Outside MoneyTown in the next period.

Draw the MDP graphically

Using a discount factor of .8, solve the MDP using value iteration (until the values have become reasonably stable). You should start with the values set to zero. You should show both the optimal policy and the optimal values.

Using a discount factor of .8, solve the MDP using policy iteration (until you have complete convergence). You should start with the policy that never drives. Again, you should show both the optimal policy and the optimal values (and of course they should be the same as in 2...).
