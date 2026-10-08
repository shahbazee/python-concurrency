def simpel_app(environ, start_response):
    stats = '200 ok'
    header = [('content-Type', 'text/plain')]
    start_response(status, header)
    return [b'Hello from WSGI']

