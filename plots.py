import matplotlib.pyplot as plt
import matplotlib.animation as anim
import numpy as np
import seaborn as sns

def setup():
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    return fig, ax

def animate(xs, ys, fig, ax):
    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)