from collections import namedtuple
from flask import render_template
from flask import request
from flask import escape
from flaskr.db import get_db, execute

#  HelperFunctions
def viewUsersHelper(conn):
    return execute(conn, "SELECT user_id, fname, email, phone FROM Users")

#  RenderFunctions
def views(bp):
    @bp.route("/users")
    def viewUsers():
        with get_db() as conn:
            rows = viewUsersHelper(conn)
        return render_template("table.html", name="Users", rows=rows)
