from flask import current_app
from queue import Queue
from threading import Thread
from app.chat.callbacks.stream import StreamingHandler

class Streamable:
 def stream(self, input):
    queue = Queue()
    handler = StreamingHandler(queue)

    def task(app_context):
        app_context.push()
        self(input, callbacks=[handler])

    Thread(target=task, args = [current_app.app_content()]).start()

    while True:
        token = queue.get()
        if token is None:
            break
        yield token