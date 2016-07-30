import matplotlib.pyplot as plt
from sklearn.svm import OneClassSVM

from fixtures import get_data, parse_to_flat

data = get_data()
X = parse_to_flat(data)

ages = [item['user']['age'] for item in data]
hs = [item['loginHistory']['24hoursSuccess'] for item in data]

plt.plot([x[0] for x in X], [x[1] for x in X], 'bo')
plt.plot(10, 1, 'ro')
# plt.show()

cls = OneClassSVM(nu=0.1, gamma=0.0)
cls.fit(X)
predict = cls.predict([[1, 10], [10, 1]])
print predict
