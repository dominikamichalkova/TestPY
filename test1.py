import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C,S = np.cos(X), np.sin(X)

plt.plot(X,C,color='green',linestyle='dashed')
plt.plot(X,S,color='blue',marker='o',markerfacecolor='red')

plt.show()

help(plt.plot)


