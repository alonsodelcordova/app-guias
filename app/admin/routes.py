from . import admin as view
from flask import request, flash, url_for, redirect,render_template,g

from app.models.Cliente import Cliente

from app.models.Cargo import Cargo

from app.models.Usuario import Usuario
from app.models.Persona import Persona

from app.models.Oficina import Oficina

from app.models.TipoMoneda import TipoMoneda
from app.models.Factura import Factura
from app.models.Pregunta import Pregunta


@view.route("/admin")
def admin():
    cargos=Cargo.query.order_by(Cargo.id).all()
    personas=Persona.query.order_by(Persona.id).all()
    facturas=Factura.query.order_by(Factura.id).all()
    clientes=Cliente.query.all()
    claves ={
        'cargos':len([(row) for row in cargos]),
        'clientes':len([(row) for row in clientes]),
        'guias':sum([len(row.guias) for row in facturas]),
        'facturas':len([(row) for row in facturas]),
        'personas':len([(row) for row in personas])
    }
    return render_template("admin/index.html",
                cargos=cargos,personas=personas,
                facturas=facturas,claves=claves)

@view.route("/cargo", methods=["GET"])
def cargo():
    list_cargo=Cargo.query.order_by(Cargo.id).all()
    return render_template("admin/cargo.html",list_cargo=list_cargo)

@view.route("/cargo", methods=["POST"])
def postCargo():
    if request.form["id"] != "": #update
        id=request.form["id"]
        cargo = Cargo.query.filter_by(id=id).first()
        if cargo.update_cargo(request.form):
            flash("Cargo Actualizado con exito !!")
        else:
            flash("No se puede guardar")
    else:   #guardar
        cargo = Cargo(request.form)
        if cargo.save_cargo():
            flash("Cargo guardado con exito !!")
        else:
            flash("No se puede guardar")
    return redirect(url_for("admin.cargo"))


@view.route("/usuario/<int:id>", methods=["GET"])
def usuario(id):
    persona=Persona.query.filter_by(id=id).first()
    list_oficina = Oficina.query.order_by(Oficina.id).all()
    list_cargo = Cargo.query.order_by(Cargo.id).all()
    return render_template("admin/usuario.html",persona=persona, list_oficina=list_oficina, list_cargo=list_cargo)

@view.route("/usuario/<int:id>", methods=["POST"])
def postusuario(id):
    if request.form["id"] != "": #update
        id_usuario=request.form["id"]
        usuario = Usuario.query.filter_by(id=id_usuario).first()
        usuario.id_persona=id
        if usuario.change_usuario(request.form):
            flash("Usuario Actualizado con exito !!")
        else:
            flash("No se puede guardar")
    else:   #guardar
        usuario = Usuario(request.form)
        usuario.id_persona=id
        if usuario.save_usuario():
            flash("usuario guardado con exito !!")
        else:
            flash("No se puede guardar")
    return redirect(url_for("admin.usuario", id=id))

@view.route("/persona", methods=["GET"])
def persona():
    list_persona=Persona.query.order_by(Persona.id).all()
    return render_template("admin/persona.html",list_persona=list_persona)

@view.route("/persona", methods=["POST"])
def postpersona():
    if request.form["id"] != "": #update
        id_persona=request.form["id"]
        persona = Persona.query.filter_by(id=id_persona).first()
        if persona.update_persona(request.form):
            flash("Persona Actualizado con exito !!")
        else:
            flash("No se puede guardar")
    else:   #guardar
        persona = Persona(request.form)
        if persona.save_persona():
            flash("persona guardado con exito !!")
        else:
            flash("No se puede guardar")
    return redirect(url_for("admin.persona"))



@view.route("/oficina", methods=["GET"])
def oficina():
    oficinas=Oficina.query.order_by(Oficina.id).all()
    return render_template("admin/oficina.html",oficinas=oficinas)

@view.route("/oficina", methods=["POST"])
def postoficina():
    if request.form["id"] != "": #update
        id_oficina=request.form["id"]
        oficina = Oficina.query.filter_by(id=id_oficina).first()
        if oficina.update_oficina(request.form):
            flash("Oficina Actualizado con exito !!")
        else:
            flash("No se puede guardar")
    else:   #guardar
        oficina = Oficina(request.form)
        if oficina.save_oficina():
            flash("oficina guardado con exito !!")
        else:
            flash("No se puede guardar")
    return redirect(url_for("admin.oficina"))

@view.route("/tipo-moneda", methods=["GET"])
def tipo_moneda():
    list_moneda=TipoMoneda.query.order_by(TipoMoneda.id).all()
    return render_template("admin/tipo-moneda.html",list_moneda=list_moneda)

@view.route("/tipo-moneda", methods=["POST"])
def posttipomoneda():
    if request.form["id"] != "": #update
        id_moneda=request.form["id"]
        moneda = TipoMoneda.query.filter_by(id=id_moneda).first()
        if moneda.update_moneda(request.form):
            flash("Tipo de Moneda Actualizada con exito !!")
        else:
            flash("No se puede guardar")
    else:
        moneda = TipoMoneda(request.form)
        if moneda.save_moneda():
            flash("Moneda guardada con exito !!")
        else:
            flash("No se puede guardar")
    return redirect(url_for("admin.tipo_moneda"))


@view.route("/pregunta", methods=["GET"])
def pregunta():
    preguntas=Pregunta.query.order_by(Pregunta.id).all()
    list_usuario=Usuario.query.order_by(Usuario.id).all()
    return render_template("admin/pregunta.html",preguntas=preguntas,list_usuario=list_usuario)

@view.route("/pregunta", methods=["POST"])
def postpregunta():
    if request.form["id"] != "": #update
        id_pregunta=request.form["id"]
        pregunta = Pregunta.query.filter_by(id=id_pregunta).first()
        if pregunta.update_pregunta(request.form):
            flash("Pregunta Actualizada con exito !!")
        else:
            flash("No se puede guardar")
    else:
        pregunta = Pregunta(request.form)
        if pregunta.save_pregunta():
            flash("Pregunta guardada con exito !!")
        else:
            flash("No se puede guardar")
    return redirect(url_for("admin.pregunta"))