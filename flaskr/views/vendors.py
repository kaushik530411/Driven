from collections import namedtuple
from flask import render_template
from flask import request
from flask import escape
from flaskr.db import get_db, execute

#  HelperFunctions
def viewVendorsHelper(conn):
    return execute(conn, "SELECT vendor_id, vendor_name, phone FROM Vendors")


def insertVendorInDB(conn, vendor_name, phone):
    print(vendor_name, phone)
    if vendor_name in ("", None):
        raise Exception
    return execute(
    conn,
    "INSERT INTO Vendors (vendor_name, phone) VALUES (:vendor_name, :phone);", {'vendor_name': vendor_name, 'phone': phone}
    )

def deleteVendorFromDB(conn, vendor_id):
    if vendor_id in ("", None):
        raise Exception
    return execute(
    conn,
    "DELETE FROM Vendors WHERE vendor_id = :vendor_id;", {'vendor_id': vendor_id}
    )

#  RenderFunctions
def views(bp):
    @bp.route("/vendors")
    def viewVendors():
        with get_db() as conn:
            rows = viewVendorsHelper(conn)
        return render_template("table.html", name="Vendors", rows=rows)

    @bp.route("/vendors/add", methods = ['POST', 'GET'])
    def renderAddVendorForm():
        attributes = {"VendorName" : "text", "Phone": "text" }
        return render_template("form.html", name="Add Vendor: ", URI="/vendors/add/submit",  submit_message="Add Vendor", attributes=attributes)

    @bp.route("/vendors/add/submit", methods = ['POST', 'GET'])
    def AddVendor():
        with get_db() as conn:
            vendor_name = request.form.get("VendorName")
            phone = request.form.get("Phone")
            try:
                insertVendorInDB(conn, vendor_name, phone)
            except Exception:
                return render_template("form_error.html", errors=["Your insertions did not went through check your inputs again."])
        return viewVendors()

    @bp.route("/vendors/remove")
    def removeVendor():
        with get_db() as conn:
            vendor_id = request.args.get("VendorId")
            print("Vendor ID", vendor_id)
            try:
                deleteVendorFromDB(conn, vendor_id)
            except Exception:
                return render_template("form_error.html", errors=["Your deletion did not went through check your inputs again."])
        return viewVendors()
