from gevent import monkey
monkey.patch_all() # we need to patch very early
from flaskapp import app
if __name__ == "__main__":
    app.run()
