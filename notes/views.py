from notes import app

@app.route('/')
def index():
    return 'Hello World!'