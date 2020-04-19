from collections import namedtuple
from flask import render_template
from flask import request
from flask import escape
from flaskr.db import get_db, execute

#  HelperFunctions
def viewAddressVendorsMapHelper(conn):
    return execute(conn, "SELECT vendor_id, address_id, vendor_access FROM AddressVendorsMap")

#  RenderFunctions
def views(bp):
    @bp.route("/addressvendorsmap")
    def viewAddressVendorsMap():
        with get_db() as conn:
            rows = viewAddressVendorsMapHelper(conn)
        return render_template("table.html", name="AddressVendorsMap", rows=rows)
