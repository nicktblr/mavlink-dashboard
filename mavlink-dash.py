import json
import urllib.request
import time
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import numpy as np
import seaborn

urlData = 'http://127.0.0.1:56781/mavlink/'
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

t = []
pitch = []
plotdata = []

def getData():
    webURL = urllib.request.urlopen(urlData)
    data = webURL.read()
    encoding = webURL.info().get_content_charset('utf-8')
    jsonData = json.loads(data.decode(encoding))
    return jsonData['ATTITUDE']['msg']['pitch']

def animate(i, xs, ys):
    # Add x and y to lists
    xs.append(dt.datetime.now().strftime('%H:%M:%S'))
    ys.append(getData())

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)

animate = anim.FuncAnimation(fig, animate, fargs=(t,pitch), interval=1000)
plt.show()
