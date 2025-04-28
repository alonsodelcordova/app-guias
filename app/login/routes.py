from . import login as view
from flask import session, flash, request, url_for, redirect,render_template,g
from app.models.Usuario import Usuario

@view.route("/",methods=["GET"])
def login():
    return render_template("login/index.html")

@view.route("/", methods=["POST"])
def postLogin():
    username = request.form.get("nombre")
    password = request.form.get("password")
    user = Usuario.query.filter_by(usuario=username).first()
    if user :
        if user.verify_password(password):
            session["usuario"]=user.to_json()
            if user.id_cargo == 2:
                return redirect(url_for("secretaria.secretaria"))
            elif user.id_cargo == 1:
                return redirect(url_for("gerente.gerente"))
            elif user.id_cargo == 3:
                return redirect(url_for("admin.admin"))
            else:
                return redirect(url_for("login.logout"))
        else:
            flash("Contraseña Incorrecta")
    else:
        flash("Usuario no existe")
    return redirect(url_for("login.login"))



@view.route("/logout", methods=["GET"])
def logout():
    if "usuario" in session:
        session.pop("usuario")
    return redirect(url_for("login.login"))



