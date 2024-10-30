import flask
app = flask.Flask("app")
app.route("/", lambda: "Hello world! ")
app.run("0.0.0.0", 8080)