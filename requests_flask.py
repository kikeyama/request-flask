import requests, time, os
from random import randint

http_host = os.environ.get('HTTP_HOST', 'localhost')
http_port = os.environ.get('HTTP_PORT', '443')
http_scheme = os.environ.get('HTTP_SCHEME', 'https')

domain = '%s://%s:%s' % (http_scheme, http_host, http_port)
paths = ['/', '/api/apm', '/api/trace']
params = ['orange', 'apple', 'banana', 'strawberry', 'error']

while(1):
    path = paths[randint(0, len(paths) - 1)]
    url = domain + path
    if path == "/":
        param = {'name':params[randint(0, len(params) - 1)]}
        try:
            res = requests.get(url, params=param)
        except:
            time.sleep(30)
    else:
        try:
            res = requests.get(url)
        except:
            time.sleep(30)
    sleep_ms = float(randint(100, 1000))
    sleep_s = sleep_ms / 1000
#    print sleep_s
#    time.sleep(0.1)
    time.sleep(sleep_s)
