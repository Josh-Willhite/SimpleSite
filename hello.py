from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_Janrain():

    return "Hello Bamboo!!"

if __name__ == "__main__":
    app.run()
