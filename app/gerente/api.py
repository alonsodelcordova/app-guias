from . import api_gerente as api
from app.models.GuiaRemision import GuiaRemision
from app.models.MotivoTraslado import MotivoTraslado
from app.models.Factura import Factura
from app import db
from sqlalchemy import func
from flask import jsonify

#********************* ventas -> Año, mes y Monto
@api.route("/ventas/<int:year>", methods=["GET"])
@api.route("/ventas", methods=["GET"])
def ventas(year=0):
    if year==0:
        facturas=db.engine.execute("SELECT year(fecha_emision) as año, month(fecha_emision) as  mes, sum(total) FROM factura GROUP BY año,mes order by año desc")
    else:
        facturas=db.engine.execute(f"SELECT  year(fecha_emision) as año, month(fecha_emision) as mes, sum(total) FROM factura WHERE year(fecha_emision) = {year}  GROUP BY año,mes order by año desc")
    data=[]

    for row in facturas:
        data.append(
            {
                'year':int(row[0]),
                'mes':int(row[1]),
                'monto':row[2]
            }
        )
    return jsonify(data)

@api.route("/guias", methods=["GET"])
def guias():
    guias=GuiaRemision.query.with_entities(MotivoTraslado.nombre_motivo, func.count(GuiaRemision.id_motivo_traslado)).join(MotivoTraslado).group_by(MotivoTraslado.nombre_motivo).all()
    data = []
    for row in guias:
        data.append([row[0], row[1]])
    
    return jsonify(data)


@api.route("/years", methods=["GET"])
def get_years():
    years = db.engine.execute("SELECT year(fecha_emision) as año FROM factura GROUP BY año order by año desc")
    data = []
    for row in years:
        data.append(row[0])
    return jsonify(data)