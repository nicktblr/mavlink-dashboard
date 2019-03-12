import matplotlib.pyplot as plt
import matplotlib.animation as anim
import numpy as np

# def animate(xs, ys, fig, ax):
#     # Draw x and y lists
#     ax.clear()
#     for n in range(0,len(xs)):
#         if len(xs[n]) > 10:
#             fit = np.polyfit(xs[n],ys[n],1)
#             fit_fn = np.poly1d(fit)
#             ax.plot(xs[n], ys[n], 'o', xs[n], fit_fn(xs[n]), '--', label="Station " + str(n+1))
#         else:
#             ax.plot(xs[n], ys[n], 'o', label="Station " + str(n+1))