import matplotlib.pyplot as plt
import numpy as np
from sklearn import svm

from data import get_data, parse_to_flat_features

plt.figure(dpi=190)

data = get_data()
faltted = parse_to_flat_features(data)

plt.plot([x[0] for x in faltted], [x[1] for x in faltted], 'bo')

xx, yy = np.meshgrid(np.linspace(-5, 250, 500), np.linspace(-5, 250, 500))

# Generate train data
X_train = np.array(faltted)
X_outliers = np.array([[10, 1]])

# fit the model
clf = svm.OneClassSVM(nu=0.1, gamma=0.1, tol=2)
clf.fit(X_train)
for i in range(2, 30):
    for j in range(2, 10):
        predict = clf.predict([[i, j]])
        shape = 'vr' if predict[0] == -1 else 'vg'
        plt.plot(i, j, shape)


# plot the line, the points, and the nearest vectors to the plane
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.contourf(xx, yy, Z, levels=np.linspace(Z.min(), 0, 10), cmap=plt.cm.Blues_r)
plt.contour(xx, yy, Z, levels=[0], linewidths=2, colors='red')
plt.contourf(xx, yy, Z, levels=[0, Z.max()], colors='orange')

plt.xlim((-5, 60))
plt.ylim((-5, 20))
plt.title("Find the outliers")

plt.show()
