import json
import urllib.request
import time
urlData = 'http://127.0.0.1:56781/mavlink/'

while True:
    webURL = urllib.request.urlopen(urlData)
    data = webURL.read()
    encoding = webURL.info().get_content_charset('utf-8')
    jsonData = json.loads(data.decode(encoding))
    print(jsonData['ATTITUDE']['msg']['pitch'])
    time.sleep(0.1)


    



