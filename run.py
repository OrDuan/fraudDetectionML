import matplotlib.pyplot as plt
import numpy as np
from sklearn import svm

from fixtures import USERS_FIXTURE


class FraudDetector(object):
    def __init__(self, dpi, nu=0.1, gamma=0.1, tol=2):
        self.fig = plt.figure(dpi=dpi)

        self.get_data()
        self.features = []
        self.generate_features_list()
        self.clf = svm.OneClassSVM(nu=nu, gamma=gamma, tol=tol)
        plt.xlim((-5, 60))
        plt.ylim((-5, 20))
        plt.title("Find The Outliers")

    def run(self):
        self.train()
        self.plot_decision_function()
        self.plot_train()
        self.plot_predicts()
        self.show()

    def generate_features_list(self):
        """
        For now I use only 2 features, can add more easly.
        """
        results = []
        for item in self.data:
            self.features.append([
                item['user']['age'],
                item['loginHistory']['30daysSuccess'],
            ])
        return results

    def get_data(self):
        """
        Using some fixture data, should be override with real data
        """
        self.data = USERS_FIXTURE

    def train(self):
        self.clf.fit(self.features)

    def plot_predicts(self):
        """
        Predict some testing data and plot it as triangles.
        """
        # fit the model
        for i in range(2, 30):
            for j in range(2, 10):
                predict = self.clf.predict([[i, j]])
                shape = 'vr' if predict[0] == -1 else 'vg'
                plt.plot(i, j, shape)

    def plot_train(self):

        plt.plot([x[0] for x in self.features], [x[1] for x in self.features], 'bo')

    def plot_decision_function(self):
        xx, yy = np.meshgrid(np.linspace(-5, 250, 500), np.linspace(-5, 250, 500))

        # plot the line, the points, and the nearest vectors to the plane
        Z = self.clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
        Z = Z.reshape(xx.shape)

        plt.contourf(xx, yy, Z, levels=np.linspace(Z.min(), 0, 10), cmap=plt.cm.Blues_r)
        plt.contour(xx, yy, Z, levels=[0], linewidths=2, colors='red')
        plt.contourf(xx, yy, Z, levels=[0, Z.max()], colors='orange')

    def show(self):
        plt.show()

if __name__ == '__main__':
    fd = FraudDetector(190)
    fd.run()
