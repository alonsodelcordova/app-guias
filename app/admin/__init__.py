from flask import Blueprint
from flask import session, request, url_for, redirect,g

admin=Blueprint('admin', __name__)
api_admin = Blueprint('api_admin', __name__,url_prefix='/api')

@admin.before_request
def before_request():
    if "usuario" in session :
        user=session["usuario"]
        if user["id_cargo"] == 2:
            return redirect(url_for("secretaria.secretaria"))
        elif user["id_cargo"] == 1:
            return redirect(url_for("gerente.gerente"))
    else:
        return redirect(url_for("login.login"))

from . import routes
from . import api