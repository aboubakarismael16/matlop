import numpy as np
import matplotlib.pyplot as plt

angle = np.linspace(0, 2 * np.pi, 150)
radius = 0.4
x = radius * np.cos(angle)
y = radius * np.sin(angle)
figure, axes = plt.subplots(1)

axes.plot(x, y)
axes.set_aspect(1)

plt.title('Parametric Equation Circle')
plt.show()