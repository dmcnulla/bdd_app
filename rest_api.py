import uvicorn
from database import Database
from fastapi import FastAPI, HTTPException
import contextlib
import time
import threading


DEFAULT_PASSWORD = 'admin'
ADMIN_USER = 'admin'
DEFAULT_ADMIN = {
    'username': ADMIN_USER,
    'password': DEFAULT_PASSWORD
}

db = Database()
app = FastAPI()


@app.get("/")
def greet():
    return {"message": "Hello, world"}


@app.get("/users")
def get_users():
    return db.get_users()


@app.get("/kill")
async def kill():
    global server
    server.keep_running = False


class Server(uvicorn.Server):
    def __init__(self, config):
        super().__init__(config)
        self.keep_running = True

    def install_signal_handlers(self):
        pass

    @contextlib.contextmanager
    def run_in_thread(self):
        thread = threading.Thread(target=self.run)
        thread.start()
        try:
            while not self.started:
                time.sleep(1e-3)
            yield
            while self.keep_running:
                time.sleep(1e-3)
        finally:
            self.should_exit = True
            thread.join()


config = uvicorn.Config("main:app", host="127.0.0.1", port=5000, log_level="info")
server = Server(config=config)


if __name__ == '__main__':
    db.add_users([DEFAULT_ADMIN])
    with server.run_in_thread():
        while server.keep_running:
            pass
