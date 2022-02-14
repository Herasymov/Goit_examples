import gevent.monkey
from urllib.request import urlopen
gevent.monkey.patch_all()
urls = ['http://www.google.com','http://translate.google.com/', 'http://www.python.org']


def print_head(url):
    print('Starting {}'.format(url))
    data = urlopen(url).read()
    print('{}: {}'.format(url, len(data)))

jobs = [gevent.spawn(print_head, _url) for _url in urls]

gevent.wait(jobs)