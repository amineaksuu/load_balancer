from simulation import run_simulation, plot_results

if __name__ == "__main__":
    # Parametreler
    TOTAL_REQUESTS = 3000
    TOTAL_SERVERS = 5
    
    # Simülasyonu Başlat
    raw_data, average_data = run_simulation(TOTAL_REQUESTS, TOTAL_SERVERS)
    
    # Sonuçları Görselleştir
    plot_results(raw_data, average_data)