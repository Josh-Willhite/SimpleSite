from flask import Flask
from flask import render_template
app = Flask(__name__)
app.config.from_envvar('FLASK_SETTINGS')

@app.route('/hello/<name>')
def hello_Janrain(name=None):
    return render_template('index.html', name=name) 

if __name__ == "__main__":
    app.run()
