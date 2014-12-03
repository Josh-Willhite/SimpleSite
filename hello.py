import os
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/hello/<name>')
def hello_Janrain(name=None):
    try:
        env  = os.environ['POC_ENV']
    except Exception as err:
        env  = 'unknown'
    
    return render_template('index.html', name=name, env=env) 

if __name__ == "__main__":
    try:
        port = os.environ['FLASK_PORT']
    except Exception as err:
        port = "5000"
    
    try:
        host = os.environ['FLASK_HOST']
    except Exception as err:
        host = '127.0.0.1'


    print "Serving on %s:%s" % (host, port)

    app.run(host=host, port=int(port))
