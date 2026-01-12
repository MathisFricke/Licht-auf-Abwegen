import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def curve_length(func_y, func_dy, x_start, x_end):
    """
    Berechnet die Bogenlänge einer Funktion y(x) im Intervall [x_start, x_end].
    L = integral( sqrt(1 + (y')^2) dx )
    """
    integrand = lambda x: np.sqrt(1 + func_dy(x)**2)
    length, error = quad(integrand, x_start, x_end)
    return length

def plot_variation_demo():
    # Start- und Endpunkte
    x_start, x_end = 0, np.pi
    y_start, y_end = 0, 0  # Wir betrachten den Weg auf der x-Achse als "Gerade"
    
    # 1. Die optimale Lösung (Gerade)
    def y_opt(x): return 0
    def dy_opt(x): return 0
    
    # 2. Die Störfunktion (Variation) eta(x) = sin(x)
    # Sie erfüllt eta(0)=0 und eta(pi)=0
    def eta(x): return np.sin(x)
    def deta(x): return np.cos(x)
    
    # Epsilon-Werte (Stärke der Störung)
    epsilons = np.linspace(-1.0, 1.0, 50)
    lengths = []
    
    # Berechne Längen für verschiedene Stärken der Störung
    for eps in epsilons:
        # y_var(x) = y_opt(x) + eps * eta(x)
        # dy_var(x) = dy_opt(x) + eps * deta(x)
        def dy_var(x, e=eps): return dy_opt(x) + e * deta(x)
        
        l = curve_length(None, dy_var, x_start, x_end)
        lengths.append(l)
        
    # --- PLOTTING ---
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Plot 1: Visualisierung der Pfade
    x_plot = np.linspace(x_start, x_end, 200)
    
    # Die "beste" Lösung
    ax1.plot(x_plot, [y_opt(x) for x in x_plot], 'k-', linewidth=3, label='Optimale Lösung (Gerade)')
    
    # Gestörte Pfade
    for eps in [-0.5, 0.5, 1.0]:
        y_vals = [y_opt(x) + eps * eta(x) for x in x_plot]
        ax1.plot(x_plot, y_vals, '--', label=f'Variation $\epsilon={eps}$')
        
    ax1.set_title(r'Variation des Pfades: $y(x) + \epsilon \cdot \eta(x)$')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.legend()
    ax1.grid(True)
    
    # Plot 2: Länge in Abhängigkeit von Epsilon
    ax2.plot(epsilons, lengths, 'r-', linewidth=2)
    ax2.set_title(r'Länge des Pfades $L(\epsilon)$')
    ax2.set_xlabel(r'Stärke der Störung $\epsilon$')
    ax2.set_ylabel('Bogenlänge')
    
    # Markiere das Minimum
    min_idx = np.argmin(lengths)
    ax2.plot(epsilons[min_idx], lengths[min_idx], 'ko', label='Minimum bei $\epsilon=0$')
    
    # Tangente bei 0 (Fréchet-Ableitung = 0)
    ax2.axhline(lengths[min_idx], color='gray', linestyle=':', label='Ableitung = 0')
    
    ax2.text(0, lengths[min_idx] + 0.05, 'Gerade ist kürzester Weg', ha='center')
    
    ax2.legend()
    ax2.grid(True)
    
    plt.tight_layout()
    plt.savefig('variation_demo.pdf')
    print("Grafik gespeichert als 'variation_demo.pdf'")

if __name__ == "__main__":
    plot_variation_demo()
