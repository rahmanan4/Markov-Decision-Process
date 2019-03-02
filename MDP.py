def transition_prob(state, action, state_prime):
    if state == 0 and action == 'drive' and state_prime == 0:
        probability = 0.9
        return probability
    elif state == 0 and action == 'drive' and state_prime == 1:
        probability = 0.1
        return probability
    elif state == 0 and action == 'wait' and state_prime == 0:
        probability = 0.7
        return probability
    elif state == 0 and action == 'wait' and state_prime == 1:
        probability = 0.3
        return probability

    elif state == 1 and action == 'drive' and state_prime == 0:
        probability = 0.3
        return probability
    elif state == 1 and action == 'drive' and state_prime == 1:
        probability = 0.6
        return probability
    elif state == 1 and action == 'drive' and state_prime == 2:
        probability = 0.1
        return probability
    elif state == 1 and action == 'wait' and state_prime == 2:
        probability = 1
        return probability

    elif state == 2 and action == 'drive' and state_prime == 0:
        probability = 0.6
        return probability
    elif state == 2 and action == 'drive' and state_prime == 2:
        probability = 0.4
        return probability
    elif state == 2 and action == 'wait' and state_prime == 2:
        probability = 1
        return probability
    else:
        return 0


def reward(action, state_prime):
    if state_prime == 0 and action == 'drive':
        reward = 20
        return reward
    elif state_prime == 0 and action == 'wait':
        reward = 30
        return reward
    elif state_prime == 1 and action == 'drive':
        reward = 0
        return reward
    elif state_prime == 1 and action == 'wait':
        reward = 10
        return reward
    elif state_prime == 2 and action == 'drive':
        reward = 0
        return reward
    elif state_prime == 2 and action == 'wait':
        reward = 10
        return reward
    else:
        return 0


def value_iteration(states, actions, disc_fac, epsilon):
    v_opt = [0, 0, 0]
    v_opt_actions = ['', '', '']
    action_values = []
    action_corresp = []
    delta = 1
    while delta > (epsilon * ((1 - disc_fac) / disc_fac)):
        v_opt_s_prime = [v for v in v_opt]
        delta = 0
        for state in states:
            for action in actions:
                q_opts = []
                for state_prime in states:
                    q_opt = transition_prob(state, action, state_prime)*(reward(action, state_prime) +
                                                             (disc_fac*v_opt[state_prime]))
                    q_opts.append(q_opt)
                action_values.append(sum(q_opts))
                action_corresp.append(action)
            v_opt[state] = max(action_values)
            max_action_index = action_values.index(max(action_values))
            max_action = action_corresp[max_action_index]
            v_opt_actions[state] = max_action
            action_values = []
            if abs(v_opt[state] - v_opt_s_prime[state]) > delta:
                delta = abs(v_opt[state] - v_opt_s_prime[state])
    return v_opt, v_opt_actions


def policy_evaluation(policy, utility, states, disc_fac):
    v_pol = utility
    action_values = []
    for state in states:
        for action in policy:
            v_opts = []
            for state_prime in states:
                v_opt = transition_prob(state, action, state_prime) * (reward(action, state_prime) +
                                                                       (disc_fac * v_pol[state_prime]))
                v_opts.append(v_opt)
            action_values.append(sum(v_opts))
        v_pol[state] = action_values[state]
        action_values = []
    return v_pol


def policy_iteration(states, actions, disc_fac):
    pol_opt = ['wait', 'wait', 'wait']
    v_pol = [0, 0, 0]
    pol_opt_s_prime = [v for v in pol_opt]
    v_pol_s_prime = [v for v in v_pol]
    action_values = []
    action_corresp = []

    unchanged = False
    while not unchanged:
        u = policy_evaluation(pol_opt, v_pol, states, disc_fac)
        unchanged = True
        for state in states:
            for action in actions:
                q_opts = []
                for state_prime in states:
                    q_opt = transition_prob(state, action, state_prime) * (reward(action, state_prime) +
                                                                    (disc_fac * v_pol_s_prime[state_prime]))
                    q_opts.append(q_opt)
                action_values.append(sum(q_opts))
                action_corresp.append(action)
            v_pol_s_prime[state] = max(action_values)
            max_action_index = action_values.index(max(action_values))
            max_action = action_corresp[max_action_index]
            action_values = []
            action_corresp = []
            if v_pol_s_prime[state] > u[state]:
                pol_opt[state] = max_action
                unchanged = False
    return v_pol_s_prime, pol_opt

# 0 = In Money Town, 1 = Money Town Suburbs, 2 = Outside Money Town
states = [0, 1, 2]
actions = ['drive', 'wait']
disc_fac = 0.8
epsilon = 0.001
print('Value Iteration: discount factor = 0.8')
print(value_iteration(states, actions, disc_fac, epsilon))
print()
print('Policy Iteration: discount factor = 0.8')
print(policy_iteration(states, actions, disc_fac))
