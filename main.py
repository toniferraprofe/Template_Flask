# inicializando
from flask import Flask

app=Flask(__name__)

# rutas
@app.route('/')
def index():
    pass



if __name__ == "__main__":
    app.run('127.0.0.1',5000,debug=True)