
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pickle

# Definicja klasy Perceptron
class Perceptron():
    def __init__(self, eta=0.01, n_iter=10):
        self.eta = eta
        self.n_iter = n_iter
    
    def fit(self, X, y):
        self.w_ = [np.random.uniform(-1.0, 1.0) for _ in range(1 + X.shape[1])]
        self.errors_ = []
        
        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(X, y):
                update = self.eta * (target - self.predict(xi))
                self.w_[1:] += update * xi
                self.w_[0] += update
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return self
    
    def net_input(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0]
    
    def predict(self, X):
        return np.where(self.net_input(X) >= 0.0, 1, -1)

# Załadowanie zbioru danych Iris
iris = load_iris()
X = iris.data[:, [0, 2]]  # wybieramy tylko pierwszą i trzecią cechę
y = (iris.target != 0) * 1  # binaryzacja problemu (0 lub 1)

# Podział na zbiór treningowy i testowy
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1, stratify=y)

# Standaryzacja cech
sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

# Trenowanie perceptronu
ppn = Perceptron(eta=0.01, n_iter=10)
ppn.fit(X_train_std, y_train)

# Zapisanie wytrenowanego modelu
with open('model.pkl', 'wb') as picklefile:
    pickle.dump(ppn, picklefile)
