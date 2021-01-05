from . import api_gerente as api
from app.models.GuiaRemision import GuiaRemision
from app.models.MotivoTraslado import MotivoTraslado
from app import db
from sqlalchemy import func
from flask import jsonify

#********************* ventas -> Año, mes y Monto
@api.route("/ventas/<int:year>", methods=["GET"])
@api.route("/ventas", methods=["GET"])
def ventas(year=0):
    if year==0:
        facturas=db.engine.execute("SELECT  EXTRACT(MONTH FROM fecha_emision) as mes, EXTRACT(YEAR FROM fecha_emision) as año, sum(total) FROM factura GROUP BY año,mes order by año,mes")
    else:
        facturas=db.engine.execute(f"SELECT  EXTRACT(MONTH FROM fecha_emision) as mes, EXTRACT(YEAR FROM fecha_emision) as año, sum(total) FROM factura WHERE extract(year from fecha_emision) = {year}  GROUP BY año,mes order by año,mes")
    data=[]

    for row in facturas:
        data.append(
            {
                'year':int(row[1]),
                'mes':int(row[0]),
                'monto':row[2]
            }
        )
    return jsonify(data)

@api.route("/guias", methods=["GET"])
def guias():
    guias=GuiaRemision.query.with_entities(MotivoTraslado.nombre_motivo, func.count(GuiaRemision.id_motivo_traslado)).join(MotivoTraslado).group_by(MotivoTraslado.nombre_motivo).all()

    return jsonify([(row) for row in guias])