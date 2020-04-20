from collections import namedtuple
from flask import render_template
from flask import request
from flask import escape
from flaskr.db import get_db, execute

#  HelperFunctions
def viewAddressHelper(conn):
    return execute(conn, "SELECT address_id, user_id, address, start_date, end_date FROM Address")

def insertAddressInDB(conn, user_id, address, start_date, end_date):
    print(user_id, address, start_date, end_date)
    invalid = ("", None)
    if not user_id or address in invalid:
        raise Exception
    return execute(
    conn,
    "INSERT INTO Address (user_id, address, start_date, end_date) VALUES (:user_id, :address, :start_date, :end_date);", {'user_id': user_id, 'address': address, 'start_date': start_date, 'end_date': end_date}
    )

#  RenderFunctions
def views(bp):
    @bp.route("/address")
    def viewAddress():
        with get_db() as conn:
            rows = viewAddressHelper(conn)
        return render_template("table.html", name="Address", rows=rows)

    @bp.route("/address/add", methods = ['POST', 'GET'])
    def renderAddAddressForm():
        attributes = {"UserId" : "number", "Address": "text", "StartDate" : "text", "EndDate" : "text" }
        return render_template("form.html", name="Add Address: ", URI="/address/add/submit",  submit_message="Add Address", attributes=attributes)

    @bp.route("/address/add/submit", methods = ['POST', 'GET'])
    def addAddress():
        with get_db() as conn:
            user_id = request.form.get("UserId")
            address = request.form.get("Address")
            start_date = request.form.get("StartDate")
            end_date = request.form.get("EndDate")
            try:
                insertAddressInDB(conn, user_id, address, start_date, end_date)
            except Exception:
                return render_template("form_error.html", errors=["Your insertions did not went through check your inputs again."])
        return viewAddress()
