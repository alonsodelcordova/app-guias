from . import api_gerente as api
from app.models.GuiaRemision import GuiaRemision
from app.models.MotivoTraslado import MotivoTraslado
from app.models.Factura import Factura
from app import db
from sqlalchemy import func, text
from flask import jsonify

#********************* ventas -> Año, mes y Monto
@api.route("/ventas/<int:year>", methods=["GET"])
@api.route("/ventas", methods=["GET"])
def ventas(year=0):
    sSQLtext = None
    if year==0:
        sSQLtext= text("SELECT EXTRACT(YEAR FROM fecha_emision) as año, EXTRACT(MONTH FROM fecha_emision) as  mes, sum(total) FROM factura GROUP BY año,mes order by año desc")
    else:
        sSQLtext = text(f"SELECT  EXTRACT(YEAR FROM fecha_emision) as año, EXTRACT(MONTH FROM fecha_emision) as mes, sum(total) FROM factura WHERE EXTRACT(YEAR FROM fecha_emision) = {year}  GROUP BY año,mes order by año desc")
    data=[]
    
    with db.engine.connect() as conn:
        facturas = conn.execute(sSQLtext)

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
    data = []
    years = None
    with db.engine.connect() as conn:
        years = conn.execute(text("SELECT EXTRACT(YEAR FROM fecha_emision) as año FROM factura GROUP BY año order by año desc"))
    for row in years:
        data.append(row[0])
    return jsonify(data)