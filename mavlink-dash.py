import json
import urllib.request
import time
import random
import datetime as dt
import plots
import matplotlib.pyplot as plt
import matplotlib.animation as anim

urlData = 'http://127.0.0.1:56781/mavlink/'

def getMavlink():
    webURL = urllib.request.urlopen(urlData)
    data = webURL.read()
    encoding = webURL.info().get_content_charset('utf-8')
    jsonData = json.loads(data.decode(encoding))
    return dt.datetime.now().strftime('%H:%M:%S'), jsonData['ATTITUDE']['msg']['pitch']

def makeData(i, time):
    return i%time, round(random.uniform(-90,90))

def getPlot(i, xs, ys):
    period = 60
    
    # FOR TESTING
    plotNumber = i//period
    x, y = makeData(i, period)
    
    if len(xs) < plotNumber+1:
        xs.append([])
        ys.append([])
    xs[plotNumber].append(x)
    ys[plotNumber].append(y)
    plots.animate(xs, ys, fig, ax)

t = []
pitch = []

plt.style.use('seaborn-darkgrid')
fig, ax = plots.setup()
animate = anim.FuncAnimation(fig, getPlot, fargs=(t,pitch), interval=1000)
plt.show()


