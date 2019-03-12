import json
import urllib.request
import time
import random
import datetime as dt
import plots
import matplotlib.pyplot as plt
import matplotlib.animation as anim

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
    plt.xlim(0,period+1)
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
    artists[station].set_data(xs, ys)
    return artists

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

xs=[]
ys=[]
period = 10

Artists = namedtuple("Artists", ("statOne", "statTwo"))
artists = Artists(
    plt.plot([],[], '.', animated=True, label='Station 1')[0],
    plt.plot([],[], '.', animated=True, label='Station 2')[0]
)

init = partial(init_fig, fig=fig, ax=ax, artists=artists)
update = partial(update_artists, artists=artists, xs=xs, ys=ys)

ani = anim.FuncAnimation(
    fig,
    update,
    frames=15,
    init_func=init,
    interval=100,
    blit=True,
    repeat=False
)
plt.show()