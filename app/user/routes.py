from . import user as view
from flask import session, request, url_for, redirect,render_template,g, flash

from app.models.Persona import Persona
from app.models.Usuario import Usuario
from app.models.Pregunta import Pregunta


@view.route("/perfil")
def perfil():
    user=session["usuario"]
    usuario=Usuario.query.filter_by(id=user["id"]).first()
    return render_template("user/perfil.html",usuario=usuario)

@view.route("/change-password")
def change_password():
    user=session["usuario"]
    usuario=Usuario.query.filter_by(id=user["id"]).first()
    return render_template("user/change-password.html",usuario=usuario)

@view.route("/verify-respuesta", methods=["POST"])
def verify_respuesta():
    id_pregunta=request.form["id_pregunta"]
    pregunta = Pregunta.query.filter_by(id=id_pregunta).first()
    user=session["usuario"]
    if pregunta and user["id"] == pregunta.id_usuario:
        respuesta=request.form["respuesta"]
        if respuesta == pregunta.respuesta :
            usuario=Usuario.query.filter_by(id=user["id"]).first()
            usuario.update_password(request.form["password"])
            if usuario.update_usuario():
                flash("Contraseña Actualizada!!")
            else:
                flash("Hubo un error al actualizar!!")
        else:
            flash("Upss. La respuesta no es correcta!!")
    else:
        flash("Tu no eres el usuario de la pregunta!!")
    return redirect(url_for("user.change_password"))

@view.route("/edit-user")
def edit_user():
    user=session["usuario"]
    usuario=Usuario.query.filter_by(id=user["id"]).first()
    return render_template("user/edit-user.html",usuario=usuario)

@view.route("/edit-user", methods=["POST"])
def postedit_user():
    user=session["usuario"]
    id_persona=user['id_persona']
    persona = Persona.query.filter_by(id=id_persona).first()
    if persona.update_persona(request.form):
        flash("Sus datos fueron actualizados con exito !!")
    else:
        flash("No se puede actualizar!!")
    return redirect(url_for("user.perfil"))
