import json
import urllib.request
import time
import random
import datetime as dt
import plots
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import numpy as np

from collections import namedtuple
from functools import partial

urlData = 'http://127.0.0.1:56781/mavlink/'
plt.style.use('seaborn-darkgrid')

def getMavlink():
    webURL = urllib.request.urlopen(urlData)
    data = webURL.read()
    encoding = webURL.info().get_content_charset('utf-8')
    jsonData = json.loads(data.decode(encoding))
    return dt.datetime.now().strftime('%H:%M:%S'), jsonData['ATTITUDE']['msg']['pitch']

def makeData(i, time):
    return i%time, round(random.uniform(-90,90)), i//time

def init_fig(fig, ax, artists):
    plt.xlim(-2,period+1)
    plt.ylim(-95,95)
    ax.set_xlabel('Time [s]')
    ax.set_ylabel('Pitch [degrees]')
    ax.legend()
    return artists

def update_artists(i, artists, xs, ys):
    x, y, station = makeData(i, period)
    if artists[station].get_xydata().size == 0:
        xs.clear()
        ys.clear()
    xs.append(x)
    ys.append(y)
    artists[2*station].set_data(xs, ys)
    if len(xs) > 10:
        fit = np.polyfit(xs,ys,1)
        fit_fn = np.poly1d(fit)
        artists[2*station+1].set_data(xs, fit_fn(xs))
    return artists

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

xs=[]
ys=[]
period = 10

Artists = namedtuple("Artists",
    ("stat1",
     "LR1",
     "stat2",
     "LR2",
     "stat3",
     "LR3",
     "stat4",
     "LR4",
     "stat5",
     "LR5",
     "stat6",
     "LR6",
     "stat7",
     "LR7",
     "stat8",
     "LR8",
     "stat9",
     "LR9",
     "stat10",
     "LR10"     
     ))
artists = Artists(
    plt.plot([],[], '.', animated=True, label='Station 1')[0],
    plt.plot([],[], '--', animated=True, label='Trend 1')[0],
    plt.plot([],[], '.', animated=True, label='Station 2')[0],
    plt.plot([],[], '--', animated=True, label='Trend 2')[0],
    plt.plot([],[], '.', animated=True, label='Station 3')[0],
    plt.plot([],[], '--', animated=True, label='Trend 3')[0],
    plt.plot([],[], '.', animated=True, label='Station 4')[0],
    plt.plot([],[], '--', animated=True, label='Trend 4')[0],
    plt.plot([],[], '.', animated=True, label='Station 5')[0],
    plt.plot([],[], '--', animated=True, label='Trend 5')[0],
    plt.plot([],[], '.', animated=True, label='Station 6')[0],
    plt.plot([],[], '--', animated=True, label='Trend 6')[0],
    plt.plot([],[], '.', animated=True, label='Station 7')[0],
    plt.plot([],[], '--', animated=True, label='Trend 7')[0],
    plt.plot([],[], '.', animated=True, label='Station 8')[0],
    plt.plot([],[], '--', animated=True, label='Trend 8')[0],
    plt.plot([],[], '.', animated=True, label='Station 9')[0],
    plt.plot([],[], '--', animated=True, label='Trend 9')[0],
    plt.plot([],[], '.', animated=True, label='Station 10')[0],
    plt.plot([],[], '--', animated=True, label='Trend 10')[0],
)

init = partial(init_fig, fig=fig, ax=ax, artists=artists)
update = partial(update_artists, artists=artists, xs=xs, ys=ys)

start = time.time()

ani = anim.FuncAnimation(
    fig,
    update,
    init_func=init,
    interval=100,
    blit=True,
    repeat=False
)
plt.show()