import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar

def gesamte_laufzeit(y_stern, n1, n2, D, x_z, y_z):
    """
    Berechnet die gesamte Laufzeit T in Abhängigkeit von y*.

    Parameter:
    y_stern (float): Schnittpunkt auf der Grenze bei x = D.
    n1 (float): Brechungsindex des Mediums 1.
    n2 (float): Brechungsindex des Mediums 2.
    D (float): x-Koordinate der Grenze zwischen den beiden Medien.
    x_z (float): x-Koordinate des Zielpunkts.
    y_z (float): y-Koordinate des Zielpunkts.

    Rückgabe:
    float: Gesamte Laufzeit.
    """
    L1 = np.sqrt(D**2 + y_stern**2)  # Weglänge im Medium 1
    L2 = np.sqrt((x_z - D)**2 + (y_z - y_stern)**2)  # Weglänge im Medium 2
    return n1 * L1 + n2 * L2

# Parameter
n1 = 1.0  # Brechungsindex des Mediums 1
n2 = 1.5  # Brechungsindex des Mediums 2
D = 3.0   # x-Koordinate der Grenze
x_z = 6.0 # x-Koordinate des Zielpunkts
y_z = 4.0 # y-Koordinate des Zielpunkts

# Bereich der y*-Werte
y_stern_werte = np.linspace(0, y_z, 500)

# Berechnung der Laufzeiten
laufzeiten = [gesamte_laufzeit(y_stern, n1, n2, D, x_z, y_z) for y_stern in y_stern_werte]

# Numerische Optimierung, um das Minimum von T(y*) zu finden
result = minimize_scalar(lambda y_stern: gesamte_laufzeit(y_stern, n1, n2, D, x_z, y_z), bounds=(0, y_z), method='bounded')
optimal_y_stern = result.x

# Plot der Gesamtlaufzeit
plt.figure(figsize=(8, 5))
plt.plot(y_stern_werte, laufzeiten, label='Gesamte Laufzeit', color='blue')
plt.axvline(x=optimal_y_stern, color='red', linestyle='--', label=f'Optimum: y* = {optimal_y_stern:.2f}')
plt.title("Gesamte Laufzeit in Abhaengigkeit vom Schnittpunkt y*")
plt.xlabel("Schnittpunkt y* (bei x = D)")
plt.ylabel("Gesamte Laufzeit")
plt.legend()
plt.grid()
plt.savefig("gesamte_laufzeit.pdf")
plt.close()

# Visualisierung des Strahlengangs
plt.figure(figsize=(8, 5))
plt.plot([0, D, x_z], [0, optimal_y_stern, y_z], label='Strahlengang', marker='o', color='blue')
plt.plot([0, x_z], [0, y_z], linestyle='--', label='Direktverbindung', color='gray')
plt.title("Visualisierung des Strahlengangs")
plt.xlabel("x")
plt.ylabel("y")
plt.axvline(x=D, color='black', linestyle='--', label='Grenze bei x = D')
plt.text(D / 2, optimal_y_stern / 2, f'n1 = {n1}', fontsize=10, color='blue')
plt.text((D + x_z) / 2, (optimal_y_stern + y_z) / 2, f'n2 = {n2}', fontsize=10, color='blue')
plt.legend()
plt.grid()
plt.savefig("strahlengang.pdf")
plt.close()
