def app(environ, start_response):
    try:
        # noinspection PyUnresolvedReferences
        import googleclouddebugger
        googleclouddebugger.enable()
    except ImportError:
        pass

    data = b"Hello, World!\n"
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])
