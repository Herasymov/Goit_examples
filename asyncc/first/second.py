import tornado.ioloop
from tornado.httpclient import AsyncHTTPClient

urls = ['http://www.google.com', 'http://translate.google.com/', 'http://www.python.org']


def handle_response(response):
    if response.error:
        print("Error:", response.error)
    else:
        url = response.request.url
        data = response.body
        print('{}: {}'.format(url, len(data)))


http_client = AsyncHTTPClient()
for url in urls:
    http_client.fetch(url, handle_response)

tornado.ioloop.IOLoop.instance().start()