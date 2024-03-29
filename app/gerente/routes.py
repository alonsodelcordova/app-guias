from . import gerente as view
from flask import session, request, url_for, redirect,render_template,g

from app.models.GuiaRemision import GuiaRemision
from app.models.Factura import Factura
from app.models.Cliente import Cliente
from app.models.MotivoTraslado import MotivoTraslado

@view.route("/gerente")
def gerente():
    facturas=Factura.query.all()
    clientes=Cliente.query.all()
    claves = {
            'monto':sum([(row.total) for row in facturas]),
            'n_guias':sum([len(row.guias) for row in facturas]),
            'n_facturas':len([(row) for row in facturas]),
            'n_clientes':len([(row) for row in clientes])
            }
    motivos=MotivoTraslado.query.all()
    return render_template("gerente/index.html",claves=claves,motivos=motivos)

@view.route("/consultar-guia/<int:id>")
@view.route("/consultar-guia")
def consultar_guia(id=0):
    if id !=0:
        factura=Factura.query.filter_by(id=id).first()
        list_guia=factura.guias
        return render_template("gerente/consultar-guia.html",factura=factura,list_guia=list_guia)
    list_guia=GuiaRemision.query.order_by(GuiaRemision.id).all()
    return render_template("gerente/consultar-guia.html",list_guia=list_guia)

@view.route("/imprimir-guia/<int:id>")
def imprimir_guia(id):
    guia=GuiaRemision.query.filter_by(id=id).first()
    return render_template("base/imprimir-guia.html",guia=guia)

@view.route("/consultar-factura")
def consultar_factura():
    list_factura=Factura.query.order_by(Factura.id).all()
    return render_template("gerente/consultar-factura.html",list_factura=list_factura)

