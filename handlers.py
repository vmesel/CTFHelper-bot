from bottery import handlers

from views import start, hashid


msghandlers = [
    handlers.message('/start', start),
    handlers.startswith('/hashid', hashid),
]
