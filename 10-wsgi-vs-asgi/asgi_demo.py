async def simple_app(scrope, receive, send):
    await send({
        'type': 'http.response.start',
        'status': 200,
        'header': [(b'content-type', b'text/plain')],
    })
    await send ({
        'type': 'http.response.body',
        'body': b'Hello From ASGI'
    })

