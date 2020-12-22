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
    menus=Menu.query.filter_by(id_cargo=2).all()
    return render_template("secretaria/index.html",menus=menus)

@view.route("/cliente")
def cliente():
    menus=Menu.query.filter_by(id_cargo=2).all()
    list_cliente = Cliente.query.all()
    return render_template("secretaria/cliente.html",list_cliente=list_cliente,menus=menus)

@view.route("/cliente", methods=["POST"])
def postcliente():
    cliente = Cliente(request.form)
    if cliente.save_cliente():
        flash("cliente guardado con exito !!")
    else:
        flash("No se puede guardar")
    return redirect(url_for("secretaria.cliente"))

@view.route("/transportista")
def transportista():
    menus=Menu.query.filter_by(id_cargo=2).all()
    list_transportista=Transportista.query.all()
    return render_template("secretaria/transportista.html",list_transportista=list_transportista,menus=menus)

@view.route("/transportista", methods=["POST"])
def posttransportista():
    transportista = Transportista(request.form)
    if transportista.save_transportista():
        flash("Transportista guardado con exito !!")
    else:
        flash("No se puede guardar")
    return redirect(url_for("secretaria.transportista"))

@view.route("/vehiculo")
def vehiculo():
    menus=Menu.query.filter_by(id_cargo=2).all()
    list_vehiculo=Vehiculo.query.all()
    return render_template("secretaria/vehiculo.html",list_vehiculo=list_vehiculo ,menus=menus)

@view.route("/vehiculo", methods=["POST"])
def postvehiculo():
    vehiculo = Vehiculo(request.form)
    if vehiculo.save_vehiculo():
        flash("vehiculo guardado con exito !!")
    else:
        flash("No se puede guardar")
    return redirect(url_for("secretaria.vehiculo"))



@view.route("/motivo-traslado")
def motivo_traslado():
    menus=Menu.query.filter_by(id_cargo=2).all()
    list_motivo=MotivoTraslado.query.all()
    return render_template("secretaria/motivo-traslado.html",list_motivo=list_motivo,menus=menus)

@view.route("/motivo-traslado", methods=["POST"])
def postmotivo():
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
    list_factura=Factura.query.all()
    return render_template("secretaria/factura.html",menus=menus,clientes=clientes,monedas=monedas,list_factura=list_factura)

@view.route("/factura", methods=["POST"])
def postfactura():
    factura = Factura(request.form)
    if factura.save_factura():
        flash("Factura guardado con exito !!")
    else:
        flash("No se puede guardar")
    return redirect(url_for("secretaria.guia",id=factura.id))

@view.route("/guia/<int:id>")
@view.route("/guia")
def guia(id=0):
    menus=Menu.query.filter_by(id_cargo=2).all()
    oficinas=Oficina.query.all()
    transportistas=Transportista.query.all()
    vehiculos= Vehiculo.query.all()
    motivos = MotivoTraslado.query.all()
    
    if id==0:
        facturas=Factura.query.all()
        list_guia = GuiaRemision.query.all()
        return render_template("secretaria/guia.html",
            menus=menus, oficinas=oficinas, facturas=facturas,
            transportistas=transportistas,
            vehiculos=vehiculos, motivos=motivos, list_guia=list_guia
            )
    else:
        factura=Factura.query.filter_by(id=id).first()
        list_guia=factura.guias
        return render_template("secretaria/guia.html",
            menus=menus, oficinas=oficinas, factura=factura, 
            transportistas=transportistas,
            vehiculos=vehiculos, motivos=motivos,list_guia=list_guia
            )
    pass

@view.route("/guia", methods=["POST"])
@view.route("/guia/<int:id>", methods=["POST"])
def postguia(id=0):
    guia = GuiaRemision(request.form)
    usuario=session["usuario"]
    guia.id_usuario = usuario["id"]
    if id!=0:
        guia.id_factura=id
    if guia.save_guia():
        flash("guia guardado con exito !!")
    else:
        flash("No se puede guardar")
        return redirect(url_for("secretaria.guia",id=id))
    return redirect(url_for("secretaria.descripcion_guia",id=guia.id))



@view.route("/descripcion-guia/<int:id>")
def descripcion_guia(id):
    menus=Menu.query.filter_by(id_cargo=2).all()
    guia=GuiaRemision.query.filter_by(id=id).first()
    return render_template("secretaria/descripcion-guia.html",guia=guia,menus=menus)

@view.route("/descripcion-guia/<int:id>", methods=["POST"])
def postdescripcion_guia(id):
    descripcion = DescripcionGuia(request.form)
    descripcion.id_guia_remision=id
    if descripcion.save_descripcion():
        flash("Descripcion de Guia guardado con exito !!")
    else:
        flash("No se puede guardar")
    return redirect(url_for("secretaria.descripcion_guia",id=id))