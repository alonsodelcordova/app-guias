from . import user as view
from flask import session, request, url_for, redirect,render_template,g, flash

from app.models.Menu import Menu

from app.models.Persona import Persona
from app.models.Usuario import Usuario


@view.route("/perfil")
def perfil():
    user=session["usuario"]
    menus=Menu.query.filter_by(id_cargo=user["id_cargo"]).all()
    usuario=Usuario.query.filter_by(id=user["id"]).first()
    return render_template("user/perfil.html",menus=menus,usuario=usuario)
