import requests, time, os
from random import randint

http_host = os.environ.get('HTTP_HOST', 'localhost')
http_port = os.environ.get('HTTP_PORT', '443')

domain = 'http://%s:%s' % (http_host, http_port)
paths = ['/', '/api/apm', '/api/trace']
params = ['orange', 'apple', 'banana', 'strawberry', 'error']

while(1):
    path = paths[randint(0, len(paths) - 1)]
    url = domain + path
    if path == "/":
        param = {'name':params[randint(0, len(params) - 1)]}
        res = requests.get(url, params=param)
    else:
        res = requests.get(url)
    sleep_ms = float(randint(100, 1000))
    sleep_s = sleep_ms / 1000
#    print sleep_s
#    time.sleep(0.1)
    time.sleep(sleep_s)
