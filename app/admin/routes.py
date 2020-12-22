from . import admin as view
from flask import session, request, flash, url_for, redirect,render_template,g

from app.models.Cargo import Cargo
from app.models.Menu import Menu
from app.models.Link import Link

from app.models.Usuario import Usuario
from app.models.Persona import Persona

from app.models.Departamento import Departamento
from app.models.Provincia import Provincia
from app.models.Distrito import Distrito
from app.models.Oficina import Oficina

from app.models.TipoMoneda import TipoMoneda
from app.models.Factura import Factura
@view.route("/admin")
def admin():
    menus=Menu.query.filter_by(id_cargo=3).all()
    list_menus=Menu.query.all()
    #usuarios=Usuario.query.filter(Usuario.usuario.ilike('%alonso%')).count()
    cargos=Cargo.query.all()
    personas=Persona.query.all()
    facturas=Factura.query.all()
    return render_template("admin/index.html",menus=menus,list_menus=list_menus,cargos=cargos,personas=personas,facturas=facturas)

@view.route("/cargo", methods=["GET"])
def cargo():
    list_cargo=Cargo.query.all()
    menus=Menu.query.filter_by(id_cargo=3).all()
    return render_template("admin/cargo.html",list_cargo=list_cargo,menus=menus)

@view.route("/cargo", methods=["POST"])
def postCargo():
    cargo = Cargo(request.form)
    if cargo.save_cargo():
        flash("Cargo guardado con exito !!")
    else:
        flash("No se puede guardar")
    return redirect(url_for("admin.cargo"))

@view.route("/menu/<int:id>", methods=["GET"])
@view.route("/menu", methods=["GET"])
def menu(id=0):
    menus=Menu.query.filter_by(id_cargo=3).all()
    if id != 0:
        cargo=Cargo.query.filter_by(id=id).first()
        list_menu=cargo.menus
        return render_template("admin/menu.html",menus=menus,list_menu=list_menu,cargo=cargo)
    list_menu=Menu.query.all()
    list_cargo=Cargo.query.all()
    return render_template("admin/menu.html",menus=menus, list_menu=list_menu,list_cargo=list_cargo)

@view.route("/menu/<int:id>", methods=["POST"])
@view.route("/menu", methods=["POST"])
def postmenu(id=0):
    menu = Menu(request.form)
    if id!=0:
        menu.id_cargo=id
    if menu.save_menu():
        flash("Menu guardado con exito !!")
    else:
        flash("No se puede guardar")
    return redirect(url_for("admin.link",id=menu.id))

@view.route("/link/<int:id>", methods=["GET"])
def link(id):
    menu=Menu.query.filter_by(id=id).first()
    menus=Menu.query.filter_by(id_cargo=3).all()
    return render_template("admin/link.html",menus=menus,menu=menu)

@view.route("/link/<int:id>", methods=["POST"])
def postlink(id):
    link = Link(request.form)
    link.id_menu=id
    if link.save_link():
        flash("link guardado con exito !!")
    else:
        flash("No se puede guardar")
    return redirect(url_for("admin.link",id=id))

@view.route("/usuario/<int:id>", methods=["GET"])
def usuario(id):
    persona=Persona.query.filter_by(id=id).first()
    menus=Menu.query.filter_by(id_cargo=3).all()
    list_oficina = Oficina.query.all()
    list_cargo = Cargo.query.all()
    return render_template("admin/usuario.html",persona=persona,menus=menus, list_oficina=list_oficina, list_cargo=list_cargo)

@view.route("/usuario/<int:id>", methods=["POST"])
def postusuario(id):
    usuario = Usuario(request.form)
    usuario.id_persona=id
    if usuario.save_usuario():
        flash("usuario guardado con exito !!")
    else:
        flash("No se puede guardar")
    return redirect(url_for("admin.usuario", id=id))

@view.route("/persona", methods=["GET"])
def persona():
    list_departamento = Departamento.query.all()
    list_persona=Persona.query.all()
    menus=Menu.query.filter_by(id_cargo=3).all()
    return render_template("admin/persona.html",list_departamento=list_departamento,list_persona=list_persona,menus=menus)

@view.route("/persona", methods=["POST"])
def postpersona():
    persona = Persona(request.form)
    if persona.save_persona():
        flash("persona guardado con exito !!")
    else:
        flash("No se puede guardar")
    return redirect(url_for("admin.persona"))

@view.route("/departamento", methods=["GET"])
def departamento():
    list_departamento=Departamento.query.all()
    menus=Menu.query.filter_by(id_cargo=3).all()
    return render_template("admin/departamento.html",list_departamento=list_departamento,menus=menus)

@view.route("/departamento", methods=["POST"])
def postdepartamento():
    departamento = Departamento(request.form)
    if departamento.save_departamento():
        flash("Departamento guardado con exito !!")
    else:
        flash("No se puede guardar")
    return redirect(url_for("admin.departamento"))

@view.route("/provincia/<int:id>", methods=["GET"])
def provincia(id):
    departamento=Departamento.query.filter_by(id=id).first()
    menus=Menu.query.filter_by(id_cargo=3).all()
    return render_template("admin/provincia.html",menus=menus,departamento=departamento)

@view.route("/provincia/<int:id>", methods=["POST"])
def postprovincia(id):
    provincia = Provincia(request.form)
    provincia.id_departamento=id
    if provincia.save_provincia():
        flash("Provincia guardado con exito !!")
    else:
        flash("No se puede guardar")
    return redirect(url_for("admin.provincia",id=id))

@view.route("/distrito/<int:id>", methods=["GET"])
def distrito(id):
    provincia=Provincia.query.filter_by(id=id).first()
    menus=Menu.query.filter_by(id_cargo=3).all()
    return render_template("admin/distrito.html",menus=menus,provincia=provincia)

@view.route("/distrito/<int:id>", methods=["POST"])
def postdistrito(id):
    distrito = Distrito(request.form)
    distrito.id_provincia=id
    if distrito.save_distrito():
        flash("distrito guardado con exito !!")
    else:
        flash("No se puede guardar")
    return redirect(url_for("admin.distrito",id=id))

@view.route("/oficina", methods=["GET"])
def oficina():
    oficinas=Oficina.query.all()
    list_departamento = Departamento.query.all()
    menus=Menu.query.filter_by(id_cargo=3).all()
    return render_template("admin/oficina.html",oficinas=oficinas,list_departamento=list_departamento,menus=menus)

@view.route("/oficina", methods=["POST"])
def postoficina():
    oficina = Oficina(request.form)
    if oficina.save_oficina():
        flash("oficina guardado con exito !!")
    else:
        flash("No se puede guardar")
    return redirect(url_for("admin.oficina"))

@view.route("/tipo-moneda", methods=["GET"])
def tipo_moneda():
    list_moneda=TipoMoneda.query.all()
    menus=Menu.query.filter_by(id_cargo=3).all()
    return render_template("admin/tipo-moneda.html",list_moneda=list_moneda,menus=menus)

@view.route("/tipo-moneda", methods=["POST"])
def posttipomoneda():
    moneda = TipoMoneda(request.form)
    if moneda.save_moneda():
        flash("Moneda guardado con exito !!")
    else:
        flash("No se puede guardar")
    return redirect(url_for("admin.tipo_moneda"))