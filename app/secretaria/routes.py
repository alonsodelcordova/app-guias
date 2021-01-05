from . import secretaria as view
from flask import session, request, url_for, redirect,render_template,g, flash

from app.models.Menu import Menu
from app.models.Cliente import Cliente
from app.models.Transportista import Transportista
from app.models.Vehiculo import Vehiculo
from app.models.GuiaRemision import GuiaRemision
from app.models.Factura import Factura
from app.models.MotivoTraslado import MotivoTraslado
from app.models.TipoMoneda import TipoMoneda

from app.models.Oficina import Oficina
from app.models.DescripcionGuia import DescripcionGuia
from app.models.Usuario import Usuario


@view.route("/secretaria")
def secretaria():
    user=session["usuario"]
    menus=Menu.query.filter_by(id_cargo=2).all()
    facturas=Factura.query.all()
    clientes=Cliente.query.all()
    guias=GuiaRemision.query.filter_by(id_usuario=user["id"]).all()
    claves = {
            'n_guias':len([(row) for row in guias]),
            'n_facturas':len([(row) for row in facturas]),
            'n_clientes':len([(row) for row in clientes])
            }
    motivos=MotivoTraslado.query.all()
    return render_template("secretaria/index.html",motivos=motivos,menus=menus,claves=claves)

@view.route("/cliente")
def cliente():
    menus=Menu.query.filter_by(id_cargo=2).all()
    list_cliente = Cliente.query.order_by(Cliente.id).all()
    return render_template("secretaria/cliente.html",list_cliente=list_cliente,menus=menus)

@view.route("/cliente", methods=["POST"])
def postcliente():
    if request.form["id"] != "": #update
        id_cliente=request.form["id"]
        cliente = Cliente.query.filter_by(id=id_cliente).first()
        if cliente.change_cliente(request.form):
            flash("Cliente Actualizado con exito !!")
        else:
            flash("No se puede guardar")
    else:   #guardar
        cliente = Cliente(request.form)
        if cliente.save_cliente():
            flash("cliente guardado con exito !!")
        else:
            flash("No se puede guardar")
    return redirect(url_for("secretaria.cliente"))

@view.route("/transportista")
def transportista():
    menus=Menu.query.filter_by(id_cargo=2).all()
    list_transportista=Transportista.query.order_by(Transportista.id).all()
    return render_template("secretaria/transportista.html",list_transportista=list_transportista,menus=menus)

@view.route("/transportista", methods=["POST"])
def posttransportista():
    if request.form["id"] != "": #update
        id_transportista=request.form["id"]
        transportista = Transportista.query.filter_by(id=id_transportista).first()
        if transportista.update_transportista(request.form):
            flash("transportista Actualizado con exito !!")
        else:
            flash("No se puede guardar")
    else:   #guardar
        transportista = Transportista(request.form)
        if transportista.save_transportista():
            flash("Transportista guardado con exito !!")
        else:
            flash("No se puede guardar")
    return redirect(url_for("secretaria.transportista"))

@view.route("/vehiculo")
def vehiculo():
    menus=Menu.query.filter_by(id_cargo=2).all()
    list_vehiculo=Vehiculo.query.order_by(Vehiculo.id).all()
    return render_template("secretaria/vehiculo.html",list_vehiculo=list_vehiculo ,menus=menus)

@view.route("/vehiculo", methods=["POST"])
def postvehiculo():
    if request.form["id"] != "": #update
        id_vehiculo=request.form["id"]
        vehiculo = Vehiculo.query.filter_by(id=id_vehiculo).first()
        if vehiculo.update_vehiculo(request.form):
            flash("vehiculo Actualizado con exito !!")
        else:
            flash("No se puede guardar")
    else:   #guardar
        vehiculo = Vehiculo(request.form)
        if vehiculo.save_vehiculo():
            flash("vehiculo guardado con exito !!")
        else:
            flash("No se puede guardar")
    return redirect(url_for("secretaria.vehiculo"))



@view.route("/motivo-traslado")
def motivo_traslado():
    menus=Menu.query.filter_by(id_cargo=2).all()
    list_motivo=MotivoTraslado.query.order_by(MotivoTraslado.id).all()
    return render_template("secretaria/motivo-traslado.html",list_motivo=list_motivo,menus=menus)

@view.route("/motivo-traslado", methods=["POST"])
def postmotivo():
    if request.form["id"] != "": #update
        id_motivo=request.form["id"]
        motivo = MotivoTraslado.query.filter_by(id=id_motivo).first()
        if motivo.update_motivo(request.form):
            flash("motivo Actualizado con exito !!")
        else:
            flash("No se puede guardar")
    else:   #guardar
        motivo = MotivoTraslado(request.form)
        if motivo.save_motivo():
            flash("Motivo de Traslado guardado con exito !!")
        else:
            flash("No se puede guardar")
    return redirect(url_for("secretaria.motivo_traslado"))

@view.route("/factura")
def factura():
    menus=Menu.query.filter_by(id_cargo=2).all()
    clientes=Cliente.query.all()
    monedas=TipoMoneda.query.all()
    list_factura=Factura.query.order_by(Factura.id).all()
    return render_template("secretaria/factura.html",menus=menus,clientes=clientes,monedas=monedas,list_factura=list_factura)

@view.route("/factura", methods=["POST"])
def postfactura():
    if request.form["id"] != "": #update
        id_factura=request.form["id"]
        factura = Factura.query.filter_by(id=id_factura).first()
        if factura.update_factura(request.form):
            flash("factura Actualizado con exito !!")
        else:
            flash("No se puede guardar")
    else:   #guardar
        factura = Factura(request.form)
        if factura.save_factura():
            flash("Factura guardado con exito !!")
        else:
            flash("No se puede guardar")
    return redirect(url_for("secretaria.factura"))

@view.route("/guia/<int:id>")
@view.route("/guia")
def guia(id=0):
    usuario=session["usuario"]
    menus=Menu.query.filter_by(id_cargo=2).all()
    oficinas=Oficina.query.all()
    transportistas=Transportista.query.all()
    vehiculos= Vehiculo.query.all()
    motivos = MotivoTraslado.query.all()
    
    if id==0:
        facturas=Factura.query.all()
        list_guia = GuiaRemision.query.order_by(GuiaRemision.id).all()
        return render_template("secretaria/guia.html",
            menus=menus, oficinas=oficinas, facturas=facturas,
            transportistas=transportistas,
            vehiculos=vehiculos, motivos=motivos, list_guia=list_guia,
            usuario=usuario
            )
    else:
        factura=Factura.query.filter_by(id=id).first()
        list_guia=factura.guias
        return render_template("secretaria/guia.html",
            menus=menus, oficinas=oficinas, factura=factura, 
            transportistas=transportistas,
            vehiculos=vehiculos, motivos=motivos,list_guia=list_guia,usuario=usuario
            )
    pass

@view.route("/guia", methods=["POST"])
@view.route("/guia/<int:id>", methods=["POST"])
def postguia(id=0):
    usuario=session["usuario"]
    if request.form["id"] != "": #update
        id_guia=request.form["id"]
        guia = GuiaRemision.query.filter_by(id=id_guia).first()
        guia.id_usuario = usuario["id"]
        if guia.update_guia(request.form):
            flash("Guia Actualizado con exito !!")
        else:
            flash("No se puede guardar")
    else:   #guardar
        guia = GuiaRemision(request.form)
        guia.id_usuario = usuario["id"]
        if id!=0:
            guia.id_factura=id
        if guia.save_guia():
            flash("guia guardado con exito !!")
        else:
            flash("No se puede guardar")
    return redirect(url_for("secretaria.guia",id=id))



@view.route("/descripcion-guia/<int:id>")
def descripcion_guia(id):
    menus=Menu.query.filter_by(id_cargo=2).all()
    guia=GuiaRemision.query.filter_by(id=id).first()
    return render_template("secretaria/descripcion-guia.html",guia=guia,menus=menus)

@view.route("/descripcion-guia/<int:id>", methods=["POST"])
def postdescripcion_guia(id):
    if request.form["id"] != "": #update
        id_descripcion=request.form["id"]
        descripcion = DescripcionGuia.query.filter_by(id=id_descripcion).first()
        descripcion.id_guia_remision=id
        if descripcion.update_descripcion(request.form):
            flash("descripcion Actualizado con exito !!")
        else:
            flash("No se puede guardar")
    else:   #guardar
        descripcion = DescripcionGuia(request.form)
        descripcion.id_guia_remision=id
        if descripcion.save_descripcion():
            flash("Descripcion de Guia guardado con exito !!")
        else:
            flash("No se puede guardar")
    return redirect(url_for("secretaria.descripcion_guia",id=id))

@view.route("/ver-guia/<int:id>")
def imprimir_guia(id):
    menus=Menu.query.filter_by(id_cargo=2).all()
    guia=GuiaRemision.query.filter_by(id=id).first()
    return render_template("base/imprimir-guia.html",menus=menus,guia=guia)