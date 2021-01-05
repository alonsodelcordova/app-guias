from . import admin as view
from flask import session, request, flash, url_for, redirect,render_template,g

from app.models.Cliente import Cliente

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
from app.models.Pregunta import Pregunta


@view.route("/admin")
def admin():
    menus=Menu.query.filter_by(id_cargo=3).all()
    list_menus=Menu.query.order_by(Menu.id).all()
    #usuarios=Usuario.query.filter(Usuario.usuario.ilike('%alonso%')).count()
    cargos=Cargo.query.order_by(Cargo.id).all()
    personas=Persona.query.order_by(Persona.id).all()
    facturas=Factura.query.order_by(Factura.id).all()
    clientes=Cliente.query.all()
    departamentos=Departamento.query.all()
    claves ={
        'cargos':len([(row) for row in cargos]),
        'clientes':len([(row) for row in clientes]),
        'departamentos':len([(row) for row in departamentos]),
        'provincias':sum([len(row.provincias) for row in departamentos]),
        'guias':sum([len(row.guias) for row in facturas]),
        'facturas':len([(row) for row in facturas]),
        'personas':len([(row) for row in personas])
    }
    return render_template("admin/index.html",
                menus=menus,list_menus=list_menus,
                cargos=cargos,personas=personas,
                facturas=facturas,claves=claves)

@view.route("/cargo", methods=["GET"])
def cargo():
    list_cargo=Cargo.query.order_by(Cargo.id).all()
    menus=Menu.query.filter_by(id_cargo=3).all()
    return render_template("admin/cargo.html",list_cargo=list_cargo,menus=menus)

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

@view.route("/menu/<int:id>", methods=["GET"])
@view.route("/menu", methods=["GET"])
def menu(id=0):
    menus=Menu.query.filter_by(id_cargo=3).all()
    if id != 0:
        cargo=Cargo.query.filter_by(id=id).first()
        list_menu=cargo.menus
        return render_template("admin/menu.html",menus=menus,list_menu=list_menu,cargo=cargo)
    list_menu=Menu.query.order_by(Menu.id).all()
    list_cargo=Cargo.query.order_by(Cargo.id).all()
    return render_template("admin/menu.html",menus=menus, list_menu=list_menu,list_cargo=list_cargo)

@view.route("/menu/<int:id>", methods=["POST"])
@view.route("/menu", methods=["POST"])
def postmenu(id=0):
    if request.form["id"] != "": #update
        id_menu=request.form["id"]
        menu = Menu.query.filter_by(id=id_menu).first()
        if menu.update_menu(request.form):
            flash("Menu Actualizado con exito !!")
        else:
            flash("No se puede guardar")
    else:   #guardar
        menu = Menu(request.form)
        if menu.save_menu():
            flash("Menu guardado con exito !!")
        else:
            flash("No se puede guardar")
    return redirect(url_for("admin.menu",id=id))

@view.route("/link/<int:id>", methods=["GET"])
def link(id):
    menu=Menu.query.filter_by(id=id).first()
    menus=Menu.query.filter_by(id_cargo=3).all()
    return render_template("admin/link.html",menus=menus,menu=menu)

@view.route("/link/<int:id>", methods=["POST"])
def postlink(id):
    if request.form["id"] != "": #update
        id_link=request.form["id"]
        link = Link.query.filter_by(id=id_link).first()
        if link.update_link(request.form):
            flash("Link Actualizado con exito !!")
        else:
            flash("No se puede guardar")
    else:   #guardar
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
    list_oficina = Oficina.query.order_by(Oficina.id).all()
    list_cargo = Cargo.query.order_by(Cargo.id).all()
    return render_template("admin/usuario.html",persona=persona,menus=menus, list_oficina=list_oficina, list_cargo=list_cargo)

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
    list_departamento = Departamento.query.order_by(Departamento.id).all()
    list_persona=Persona.query.order_by(Persona.id).all()
    menus=Menu.query.filter_by(id_cargo=3).all()
    return render_template("admin/persona.html",list_departamento=list_departamento,list_persona=list_persona,menus=menus)

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

@view.route("/departamento", methods=["GET"])
def departamento():
    list_departamento=Departamento.query.order_by(Departamento.id).all()
    menus=Menu.query.filter_by(id_cargo=3).all()
    return render_template("admin/departamento.html",list_departamento=list_departamento,menus=menus)

@view.route("/departamento", methods=["POST"])
def postdepartamento():
    if request.form["id"] != "": #update
        id_departamento=request.form["id"]
        departamento = Departamento.query.filter_by(id=id_departamento).first()
        if departamento.update_departamento(request.form):
            flash("Departamento Actualizado con exito !!")
        else:
            flash("No se puede guardar")
    else:   #guardar
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
    if request.form["id"] != "": #update
        id_provincia=request.form["id"]
        provincia = Provincia.query.filter_by(id=id_provincia).first()
        provincia.id_departamento=id
        if provincia.update_provincia(request.form):
            flash("Provincia Actualizado con exito !!")
        else:
            flash("No se puede guardar")
    else:   #guardar
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
    if request.form["id"] != "": #update
        id_distrito=request.form["id"]
        distrito = Distrito.query.filter_by(id=id_distrito).first()
        distrito.id_provincia=id
        if distrito.update_distrito(request.form):
            flash("distrito Actualizado con exito !!")
        else:
            flash("No se puede guardar")
    else:   #guardar
        distrito = Distrito(request.form)
        distrito.id_provincia=id
        if distrito.save_distrito():
            flash("distrito guardado con exito !!")
        else:
            flash("No se puede guardar")
    return redirect(url_for("admin.distrito",id=id))

@view.route("/oficina", methods=["GET"])
def oficina():
    oficinas=Oficina.query.order_by(Oficina.id).all()
    list_departamento = Departamento.query.order_by(Departamento.id).all()
    menus=Menu.query.filter_by(id_cargo=3).all()
    return render_template("admin/oficina.html",oficinas=oficinas,list_departamento=list_departamento,menus=menus)

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
    menus=Menu.query.filter_by(id_cargo=3).all()
    return render_template("admin/tipo-moneda.html",list_moneda=list_moneda,menus=menus)

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
    menus=Menu.query.filter_by(id_cargo=3).all()
    preguntas=Pregunta.query.order_by(Pregunta.id).all()
    list_usuario=Usuario.query.order_by(Usuario.id).all()
    return render_template("admin/pregunta.html",preguntas=preguntas,menus=menus,list_usuario=list_usuario)

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