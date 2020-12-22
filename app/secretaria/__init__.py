from flask import Blueprint
from flask import session, request, url_for, redirect,g

secretaria=Blueprint('secretaria', __name__)
api_secretaria = Blueprint('api_secretaria', __name__,url_prefix='/api')

@api_secretaria.before_request
@secretaria.before_request
def before_request():
    if "usuario" in session :
        user=session["usuario"]
        if user["id_cargo"] == 1:
            return redirect(url_for("gerente.gerente"))
        elif user["id_cargo"] == 3:
            return redirect(url_for("admin.admin"))
    else:
        return redirect(url_for("login.login"))

from . import routes