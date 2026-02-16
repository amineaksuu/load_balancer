import numpy as np

class Server:
    """
    Simulates a server with non-stationary and noisy response times.
    """
    def __init__(self, server_id, initial_mean_latency):
        self.server_id = server_id
        self.mean_latency = initial_mean_latency
        self.std_dev = 0.5  # Noise level
        # Drift: How much the server performance changes over time
        self.drift_rate = 0.05 

    def process_request(self):
        """
        Simulates processing a request.
        Returns: Latency (time taken)
        """
        # 1. Non-stationary behavior: Update mean latency (Random Walk)
        # Sunucu performansı zamanla rastgele iyiye veya kötüye gider.
        change = np.random.normal(0, self.drift_rate)
        self.mean_latency += change
        
        # Ensure latency doesn't become unrealistic (negative or too low)
        self.mean_latency = max(0.1, self.mean_latency)

        # 2. Noisy response: Generate actual latency from distribution
        # Gürültü eklenmiş anlık yanıt süresi
        latency = np.random.normal(self.mean_latency, self.std_dev)
        
        # Return strictly positive latency
        return max(0.01, latency)

    def __str__(self):
        return f"Server {self.server_id} (Mean Latency: {self.mean_latency:.2f}ms)"