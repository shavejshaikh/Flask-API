try:
    from flask import Flask,g
    from flask_track_usage import TrackUsage
    from flask_track_usage.storage.printer import PrintWriter
    from flask_track_usage.storage.output import OutputWriter
except Exception as e:
    print("Some modules is missing:{}".format(e))

app = Flask(__name__)
app.config['TRACK_USAGE_USE_FREEGEOIP'] = False
app.config["TRACK_USAGE_INCLUDE_OR_EXCLUDE_VIEWS"] = "include"


t = TrackUsage(app, [
    PrintWriter(),
    OutputWriter(transform=lambda s: "OUTPUT: " +str(s))
])

@t.include
@app.route("/")
def index():
    g.track_var["optional"] = "something"
    return "Hello"

if __name__ == "__main__":
    app.run(debug = True)