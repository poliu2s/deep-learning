"""Softmax."""
import numpy as np
import matplotlib.pyplot as plt

scores = [3.0, 1.0, 0.2]
testScores = np.array([[1, 2, 3, 6],
                       [2, 4, 5, 6],
                       [3, 8, 7, 6]])



def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    output = []
    denomSum = 0
    for i in range(0, len(x)):
        denomSum += np.exp(x[i])

    for j in range(0, len(x)):
        output.append(np.exp(x[j]) / denomSum)
    return np.asarray(output)


print(softmax(scores))
print(softmax(testScores))

x = np.arange(-2.0, 6.0, 0.1)
scores = np.vstack([x, np.ones_like(x), 0.2 * np.ones_like(x)])

plt.plot(x, softmax(scores).T, linewidth=2)
plt.show()