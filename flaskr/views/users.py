from collections import namedtuple
from flask import render_template
from flask import request
from flask import escape
from flaskr.db import get_db, execute

#  HelperFunctions
def viewUsersHelper(conn):
    return execute(conn, "SELECT user_id, fname, email, phone FROM Users")

def insertUserInDB(conn, fname, lname, email, phone):
    print(fname, lname, email, phone)
    invalid = ("", None)
    if fname in invalid or lname in invalid or email in invalid:
        raise Exception
    return execute(
    conn,
    "INSERT INTO Users (fname, lname, email, phone) VALUES (:fname, :lname, :email, :phone);", {'fname': fname, 'lname': lname, 'email': email, 'phone': phone}
    )

#  RenderFunctions
def views(bp):
    @bp.route("/users")
    def viewUsers():
        with get_db() as conn:
            rows = viewUsersHelper(conn)
        return render_template("table.html", name="Users", rows=rows)

    @bp.route("/users/add", methods = ['POST', 'GET'])
    def renderAddUsersForm():
        attributes = {"FirstName" : "text", "LastName": "text", "Email" : "Text", "Phone" : "Text" }
        return render_template("form.html", name="Add Users: ", URI="/users/add/submit",  submit_message="Add User", attributes=attributes)

    @bp.route("/users/add/submit", methods = ['POST', 'GET'])
    def addUsers():
        with get_db() as conn:
            fname = request.form.get("FirstName")
            lname = request.form.get("LastName")
            email = request.form.get("Email")
            phone = request.form.get("Phone")
            try:
                insertUserInDB(conn, fname, lname, email, phone)
            except Exception:
                return render_template("form_error.html", errors=["Your insertions did not went through check your inputs again."])
        return viewUsers()
