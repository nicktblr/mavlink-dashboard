import json
import urllib.request
import time
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

def getPlot(i, xs, ys):
    x, y = getMavlink()
    xs.append(x)
    ys.append(y)
    plots.animate(xs, ys, fig, ax)

t = []
pitch = []

fig, ax = plots.setup()
animate = anim.FuncAnimation(fig, getPlot, fargs=(t,pitch), interval=1000)
plt.show()
