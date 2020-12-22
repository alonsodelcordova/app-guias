from flask import Blueprint
from flask import session, request, url_for, redirect,g

gerente=Blueprint('gerente', __name__)
api_gerente = Blueprint('api_gerente', __name__,url_prefix='/api')

@api_gerente.before_request
@gerente.before_request
def before_request():
    if "usuario" in session :
        user=session["usuario"]
        if user["id_cargo"] == 2:
            return redirect(url_for("secretaria.secretaria"))
        elif user["id_cargo"] == 3:
            return redirect(url_for("admin.admin"))
    else:
        return redirect(url_for("login.login"))

from . import routes