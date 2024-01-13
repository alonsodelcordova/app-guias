var fecha = new Date();
var year = fecha. getFullYear();
mostrarVentas(year);
mostrarGuias();
function mostrarVentas(year){
    $.ajax({
        url: "/api/ventas/"+year,
        method: 'GET',
        data: {},
        cache: false,
        dataType: 'json',
        success: function (respuesta) 
        {
            var n_meses=[]
            var montos=[]
            respuesta.forEach(data => {
                n_meses.push(meses(data.mes));
                montos.push(data.monto);
            });
            areaChart(n_meses,montos);
        },
        error: function () {
            messageSweet('error',"Error del Servidor!!","Ocurrio un error inesperado");
        }
    });
}

function meses(numero){
    var data_meses = ['ENERO','FEBRERO','MARZO','ABRIL','MAYO','JUNIO','JULIO','AGOSTO',
            'SEPTIEMBRE','OCTUBRE','NOVIEMBRE','DICIEMBRE'];
    return data_meses[numero-1];
}
function cambiarYear(){
    var year = $("#year").val();
    mostrarVentas(year);
}

function mostrarGuias(){
    $.ajax({
        url: "/api/guias",
        method: 'GET',
        data: {},
        cache: false,
        dataType: 'json',
        success: function (respuesta) 
        {
            
            var n_guias=[]
            var motivos=[]
            respuesta.forEach(data => {
                n_guias.push(data[1]);
                motivos.push(data[0]);
            });
            chartPie(motivos,n_guias);
        },
        error: function () {
            messageSweet('error',"Error del Servidor!!","Ocurrio un error inesperado");
        }
    });
}

getYears();

function getYears(){
    $.ajax({
        url: "/api/years",
        method: 'GET',
        data: {},
        cache: false,
        dataType: 'json',
        success: function (respuesta) 
        {
            var html = '';
            respuesta.forEach(data => {
                html += '<option value="'+data+'">'+data+'</option>';
            });
            $("#year").html(html);
        },
        error: function () {
            messageSweet('error',"Error del Servidor!!","Ocurrio un error inesperado");
        }
    });
}