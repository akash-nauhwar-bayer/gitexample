from flask import Flask
 
app = Flask(__name__)
 
@app.route('/hello')
def hello():
    return 'Hello Akash'
 
app.run(host='localhost', port=5000)