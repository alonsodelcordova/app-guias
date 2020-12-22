from flask import Blueprint
from flask import session, request, url_for, redirect,g

login=Blueprint('login', __name__)
api_login = Blueprint('api_login', __name__,url_prefix='/api')

@login.before_request
def before_request():
    if "usuario" in session and request.endpoint not in ["login.logout"]:
        user=session["usuario"]
        if user["id_cargo"] == 2:
            return redirect(url_for("secretaria.secretaria"))
        elif user["id_cargo"] == 1:
            return redirect(url_for("gerente.gerente"))
        elif user["id_cargo"] == 3:
            return redirect(url_for("admin.admin"))
    
 

from . import routes