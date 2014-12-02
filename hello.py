import os
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/hello/<name>')
def hello_Janrain(name=None):
    return render_template('index.html', name=name) 

if __name__ == "__main__":
    try:
        port = os.environ['FLASK_PORT']
    except Exception as err:
        port = "5000"
    
    print "Serving on port: %s" % port

    app.run(port=int(port))
