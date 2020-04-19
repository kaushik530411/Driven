from flask import render_template

def views(bp):
    @bp.route("/")
    def index():
        print("__________LOG: HIT HERE __________________")
        return render_template("index.html")
