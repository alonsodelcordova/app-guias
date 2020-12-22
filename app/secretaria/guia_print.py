from fpdf import FPDF
from app.secretaria import secretaria
from datetime import datetime
from flask import make_response
from app.models.GuiaRemision import GuiaRemision

class PDF(FPDF):
    def header(self):
        # Logo
        self.image('app/static/img/logo-productos.jpg', 20, 8, 50)
        # Arial bold 15
        self.set_font('Helvetica', 'B', 20)
        # Move to the right
        self.cell(80)
        # Title
        self.cell(140, 10, 'CORPORACION AGROSECHURA PERÚ S.A.C.', 1, 0, 'C')
        fecha = datetime.now()
        self.set_font('Helvetica', 'B', 10)
        self.cell(60, 10, 'Fecha: ' + str(fecha.day) + '-' + str(fecha.month) + '-' + str(fecha.year), 1, 0, 'R')
        self.ln(10)
        self.cell(80)
        self.cell(140, 20, 'CORPORACION AGROSECHURA  SAC', 1, 0, 'C')
        # Line break
        self.ln(20)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Helvetica', 'I', 8)
        # Page number
        self.cell(0, 8, '@Agrosechura', 0, 0, 'L')
        self.cell(0, 10, 'Página ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')


@secretaria.route('/guia-imprimir/<int:id>')
def imprimir(id):
        guia = GuiaRemision.query.filter_by(id=id).first()

        pdf = PDF('L', 'mm', 'A4')
        pdf.alias_nb_pages()
        pdf.add_page(orientation='L')
        page_width = pdf.w - 2 * pdf.l_margin
        pdf.ln(10)
        pdf.set_font('Helvetica', 'B', 12)
        col_width = page_width / 6
        pdf.ln(1)
        pdf.cell(0, 0, 'CORPORACION AGROSECHURA SAC', 0, 0, 'C')
        pdf.ln(4)

        th = pdf.font_size +3
        pdf.set_fill_color(53, 160, 53)
        pdf.cell(10, th, "Nº",1,0,'C',1)
        pdf.cell(80, th, "Descripcion", 1,0,'C',1)
        pdf.cell(40, th, "Cantidad",1,0,'C',1)
        pdf.cell(40, th, "unidad de Medida", 1, 0, 'C',1)
        pdf.cell(40, th, "Peso", 1, 0, 'C',1)
        pdf.ln(th)
        for row in guia.descripcion_guias:
            pdf.cell(10, th, str(row.id), 1, 0, 'C')
            pdf.cell(80, th, row.descripcion, 1, 0, 'C')
            pdf.cell(40, th, str(row.cantidad), 1, 0, 'C')
            pdf.cell(40, th, str(row.unidad_medida), 1, 0, 'C')
            pdf.cell(40, th, str(row.peso), 1, 0, 'C')
            #pdf.cell(40, th, row.fecha_inicio.strftime('%d/%m/%Y'), 1, 0, 'C')
            pdf.ln(th)
        pdf.ln(5)
        pdf.cell(0, 0, 'CORPORACION AGROSECHURA SAC', 0, 0, 'C')

        response = make_response(pdf.output(dest='S').encode('latin-1'))
        response.headers.set('Content-Disposition', 'inline', filename="GuiaRemision.pdf")
        response.headers.set('Content-Type', 'application/pdf')
        return response
