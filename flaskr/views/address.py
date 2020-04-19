from collections import namedtuple
from flask import render_template
from flask import request
from flask import escape
from flaskr.db import get_db, execute

#  HelperFunctions
def viewAddressHelper(conn):
    return execute(conn, "SELECT address_id, user_id, address, start_date, end_date FROM Address")

#  RenderFunctions
def views(bp):
    @bp.route("/address")
    def viewAddress():
        with get_db() as conn:
            rows = viewAddressHelper(conn)
        return render_template("table.html", name="Address", rows=rows)
