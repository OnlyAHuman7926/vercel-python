import flask as mian
mmian = mian.Flask("app")
mmian.route("/", lambda mian: "int mian {<br>return 0;<br>}")
mmian.run("0.0.0.0", 8080)