from collections import namedtuple
from flask import render_template
from flask import request
from flask import escape
from flaskr.db import get_db, execute

#  HelperFunctions
def viewVendorsHelper(conn):
    return execute(conn, "SELECT vendor_id, vendor_name, phone FROM Vendors")

#  RenderFunctions
def views(bp):
    @bp.route("/vendors")
    def viewVendors():
        with get_db() as conn:
            rows = viewVendorsHelper(conn)
        return render_template("table.html", name="Vendors", rows=rows)
