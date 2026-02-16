import numpy as np

class SoftmaxLoadBalancer:
    """
    Client-side Load Balancer using Softmax Action Selection.
    Includes Numerical Stability fixes.
    """
    def __init__(self, n_servers, temperature=1.0):
        self.n_servers = n_servers
        self.temperature = temperature
        
        # Q-Values: Estimated reward (negative latency) for each server
        # Başlangıçta tüm sunucular eşit kabul edilir (Optimistic initialization yapılabilir)
        self.q_values = np.zeros(n_servers)
        
        # Action Counts: How many times each server was selected
        self.action_counts = np.zeros(n_servers)

    def select_server(self):
        """
        Selects a server using Softmax probability distribution.
        Implements numerical stability to avoid overflow.
        """
        # --- NUMERICAL STABILITY FIX ---
        # Subtract max(q) to prevent exp() from overflowing with large numbers.
        # Shift invariance property: softmax(x) = softmax(x - c)
        q_shifted = self.q_values - np.max(self.q_values)
        
        # Calculate exponentials with temperature
        exp_values = np.exp(q_shifted / self.temperature)
        
        # Calculate probabilities
        probabilities = exp_values / np.sum(exp_values)
        
        # Select server based on calculated probabilities
        selected_server = np.random.choice(range(self.n_servers), p=probabilities)
        return selected_server

    def update(self, server_idx, latency):
        """
        Updates the Q-value estimates using incremental mean formula.
        """
        # Reward is negative latency because we want to MINIMIZE latency
        # and RL maximizes reward.
        reward = -latency
        
        self.action_counts[server_idx] += 1
        n = self.action_counts[server_idx]
        
        # Incremental Update Rule:
        # NewEstimate = OldEstimate + (1/n) * (Reward - OldEstimate)
        current_q = self.q_values[server_idx]
        self.q_values[server_idx] = current_q + (1.0 / n) * (reward - current_q)