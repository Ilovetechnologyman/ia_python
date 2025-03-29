import numpy as np
import matplotlib.pyplot as plt

# Données du tableau 1
x = np.array([0.1, 0.2, 0.3, 0.3, 0.5, 0.4])
y = np.array([3.5, 5.2, 4.5, 5.3, 6.5, 4.1])

# Initialisation des paramètres
theta0 = 0  # Biais
theta1 = 0  # Pente
alpha = 0.01  # Taux d'apprentissage
epochs = 1000  # Nombre d'itérations

# Fonction coût (erreur quadratique moyenne)
def compute_cost(x, y, theta0, theta1):
    m = len(y)
    predictions = theta0 + theta1 * x
    cost = (1 / (2 * m)) * np.sum((predictions - y) ** 2)
    return cost

# Gradient descent
def gradient_descent(x, y, theta0, theta1, alpha, epochs):
    m = len(y)
    cost_history = []

    for _ in range(epochs):
        predictions = theta0 + theta1 * x
        error = predictions - y

        # Mise à jour des paramètres
        theta0 -= alpha * (1 / m) * np.sum(error)
        theta1 -= alpha * (1 / m) * np.sum(error * x)

        # Calcul du coût
        cost = compute_cost(x, y, theta0, theta1)
        cost_history.append(cost)

    return theta0, theta1, cost_history

# Apprentissage
theta0, theta1, cost_history = gradient_descent(x, y, theta0, theta1, alpha, epochs)

# Affichage des résultats
print(f"Paramètres appris : theta0 = {theta0}, theta1 = {theta1}")

# Tracé de la fonction h (initiale et finale)
plt.scatter(x, y, color='blue', label='Données')
plt.plot(x, theta0 + theta1 * x, color='red', label='Modèle appris')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Régression linéaire')
plt.show()

# Tracé de la courbe d'apprentissage
plt.plot(range(epochs), cost_history, color='green')
plt.xlabel('Époques')
plt.ylabel('Coût')
plt.title('Courbe d\'apprentissage')
plt.show()