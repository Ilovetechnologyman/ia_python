import numpy as np
import matplotlib.pyplot as plt

# Données
x1 = np.array([0.5, 0.4, 0.4, 2.3, 2.1, 2.2])
x2 = np.array([3, 3, 4, 5, 5, 4.5])
y = np.array([1, 1, 1, -1, -1, -1])

# Ajout d'une colonne de biais et regroupement des données
X = np.c_[np.ones(x1.shape[0]), x1, x2]  # Ajout d'une colonne de 1 pour le biais
y = y.reshape(-1, 1)  # Reshape pour correspondre aux dimensions

# Initialisation des poids
weights = np.zeros((X.shape[1], 1))  # [biais, w1, w2]
learning_rate = 0.1
epochs = 1000

# Fonction de prédiction
def predict(X, weights):
    return np.sign(np.dot(X, weights))

# Algorithme du perceptron
for _ in range(epochs):
    for i in range(X.shape[0]):
        prediction = predict(X[i], weights)
        if prediction != y[i]:  # Mise à jour si erreur
            weights += learning_rate * y[i] * X[i].reshape(-1, 1)

# Affichage des poids appris
print(f"Poids appris : {weights.ravel()}")

# Tracé des points
plt.scatter(x1[y.flatten() == 1], x2[y.flatten() == 1], color='blue', label='Classe 1 (y=1)')
plt.scatter(x1[y.flatten() == -1], x2[y.flatten() == -1], color='red', label='Classe -1 (y=-1)')

# Tracé de la droite de séparation
x1_line = np.linspace(0, 3, 100)
x2_line = -(weights[1] * x1_line + weights[0]) / weights[2]
plt.plot(x1_line, x2_line, color='green', label='Droite de séparation')

# Configuration du graphique
plt.xlabel('x1')
plt.ylabel('x2')
plt.legend()
plt.title('Séparation des classes avec le perceptron')
plt.grid()
plt.show()





