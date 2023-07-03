from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There! This is Technixleo sample application.</h1>"

if __name__ == "__main__":
    application.run(debug=True,host='0.0.0.0')