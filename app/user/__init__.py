from flask import Blueprint
from flask import session, request, url_for, redirect,g

user=Blueprint('user', __name__)

@user.before_request
def before_request():
    if "usuario" not in session :
        return redirect(url_for("login.login"))

from . import routes