from flask import Flask
app = Flask(__name__)

@app.route('/')
def helloIndex():
    return '<h1>Hello World</h1>'

app.run(host='0.0.0.0', port= 3000)
