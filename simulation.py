import matplotlib.pyplot as plt
import numpy as np
from server import Server
from load_balancer import SoftmaxLoadBalancer

def run_simulation(n_requests=2000, n_servers=5):
    # Initialize Servers with random starting latencies
    servers = [Server(i, np.random.uniform(1.0, 5.0)) for i in range(n_servers)]
    
    # Initialize Load Balancer
    # Temperature determines exploration vs exploitation balance
    # High Temp -> More random (Explore), Low Temp -> Greedy (Exploit)
    lb = SoftmaxLoadBalancer(n_servers, temperature=0.5)

    latencies = []
    avg_latencies = []
    selected_servers_history = []

    print("Simulation started...")
    
    for t in range(n_requests):
        # 1. Agent chooses action
        server_idx = lb.select_server()
        selected_servers_history.append(server_idx)
        
        # 2. Environment responds
        latency = servers[server_idx].process_request()
        
        # 3. Agent learns
        lb.update(server_idx, latency)
        
        # Data collection
        latencies.append(latency)
        # Calculate running average
        avg_latencies.append(np.mean(latencies))

    print("Simulation finished.")
    return latencies, avg_latencies

def plot_results(latencies, avg_latencies):
    plt.figure(figsize=(12, 6))
    
    # Plot 1: Average Latency Over Time
    plt.subplot(1, 2, 1)
    plt.plot(avg_latencies, color='red', linewidth=2, label='Average Latency')
    plt.title('System Performance Improvement')
    plt.xlabel('Request Number')
    plt.ylabel('Avg Latency (ms)')
    plt.grid(True, alpha=0.3)
    plt.legend()

    # Plot 2: Instant Latency (Scatter) to show noise
    plt.subplot(1, 2, 2)
    plt.scatter(range(len(latencies)), latencies, alpha=0.2, s=2, color='blue')
    plt.title('Instant Latency Distribution (Noise)')
    plt.xlabel('Request Number')
    plt.ylabel('Latency (ms)')
    
    plt.tight_layout()
    plt.show()