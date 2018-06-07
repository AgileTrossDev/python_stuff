# Hello World Experiment
#
# Execute:
# To run the application you can either use the flask command or python’s -m
# switch with Flask. Before you can do that you need to tell your terminal the
# application to work with by exporting the FLASK_APP environment variabl
#
# Ex:
#   $ export FLASK_APP=hello.py
#   $ flask run
################################################################################


# First we imported the Flask class. An instance of this class
# will be our WSGI application.
from flask import Flask

# Next we create an instance of this class. The first argument is the name
# of the application’s module or package. If you are using a single module
# (as in this example), you should use __name__ because depending on if it’s
# started as application or imported as module the name will be different
# ('__main__' versus the actual import name). This is needed so that Flask
# knows where to look for templates, static files, and so on. For more
# information have a look at the Flask documentation.
app = Flask(__name__)

# We then use the route() decorator to tell Flask what URL should trigger our
# function.
@app.route("/")
def index():
    return "Index Page"

# The function is given a name which is also used to generate URLs for that
# particular function, and returns the message we want to display in the
# user’s browser.
@app.route("/hello")
def hello():
    return "Hello World!"


@app.route("/greet/<uname>")
def greet(uname):
    return "Greenting %s" % uname
