import requests, time, os
import logging, sys
from random import randint

http_host = os.environ.get('HTTP_HOST', 'localhost')
http_port = os.environ.get('HTTP_PORT', '443')
http_scheme = os.environ.get('HTTP_SCHEME', 'https')

domain = '%s://%s:%s' % (http_scheme, http_host, http_port)
paths = ['/', '/api/apm', '/api/trace', '/api/post', '/lambda']
params = ['orange', 'apple', 'banana', 'strawberry', 'error']

logger = logging.getLogger()
logger.setLevel(logging.INFO)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

while(1):
    path = paths[randint(0, len(paths) - 1)]
    url = domain + path
    if path == "/":
        param = {'name':params[randint(0, len(params) - 1)]}
        try:
            logger.info('requesting ' + url + '?name=' + param['name'])
            res = requests.get(url, params=param)
            logger.info('succeeded ' + url + '?name=' + param['name'])
        except Exception as e:
            logger.error('error ' + url + '?name=' + param['name'] + '; ' + str(e))
            time.sleep(3)
            continue
    elif path == '/api/post':
        res = requests.post(url, data = {'message':'hello world'})
        logger.info('succeeded ' + url)
    else:
        try:
            logger.info('requesting ' + url)
            res = requests.get(url)
            logger.info('succeeded ' + url)
        except Exception as e:
            logger.error('error ' + url + '; ' + str(e))
            time.sleep(3)
            continue

    sleep_ms = float(randint(100, 1000))
    
    # spike for watchdog
    hour = int(time.time() % (24 * 3600) // 3600)
    divider = 1000
    if hour == 0:
        # override divider for spike
        divider = 100

    sleep_s = sleep_ms / divider
    time.sleep(sleep_s)
