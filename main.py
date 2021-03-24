import matplotlib
import numpy as np
import matplotlib.pyplot as plt

# fig1, ax = plt.subplots()
#
# ax.set_xlim(300, 400)
# ax.set_box_aspect(1)
#
# fig2, (ax, ax2) = plt.subplots(ncols=2, sharey= True)
#
# ax.plot([1,5], [0,10])
# ax2.plot([100,500],[10, 15])
#
# ax.set_box_aspect(1)
# ax2.set_box_aspect(1)

fig3, ax = plt.subplots()

ax.add_patch(plt.Circle((1,1), 1))
ax.set_aspect("equal",adjustable="datalim")
ax.set_box_aspect(0.5)
ax.autoscale()

plt.show()