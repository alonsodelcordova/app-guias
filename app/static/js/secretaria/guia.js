function editarMotivo(id){
    $.ajax({
        url: "/api/motivo/"+id,
        method: 'GET',
        data: {},
        cache: false,
        dataType: 'json',
        success: function (respuesta) 
        {
            $("#id").val(id);
            $("#exampleModalLabel").html("Actualizar motivo");
            $("#nombre").val(respuesta.nombre);
            $("#modalMotivo").modal("show");
        },
        error: function () {
            messageSweet('error',"Error del Servidor!!","Ocurrio un error inesperado");
        }
    });
}

function editarGuia(id){
    $.ajax({
        url: "/api/guia/"+id,
        method: 'GET',
        data: {},
        cache: false,
        dataType: 'json',
        success: function (respuesta) 
        {
            $("#id").val(id);
            $("#exampleModalLabel").html("Actualizar guia");
            $("#fecha_inicio").val(respuesta.fecha_inicio);
            $("#punto_destino").val(respuesta.punto_destino);
            $("#direccion").val(respuesta.direccion);
            $("#id_oficina option[value="+ respuesta.id_oficina +"]").attr("selected",true);
            $("#id_motivo_traslado option[value="+ respuesta.id_motivo_traslado +"]").attr("selected",true);
            $("#id_transportista option[value="+ respuesta.id_transportista +"]").attr("selected",true);
            $("#id_vehiculo option[value="+ respuesta.id_vehiculo +"]").attr("selected",true);
            $("#id_factura option[value="+ respuesta.id_factura +"]").attr("selected",true);
            $("#modalGuia").modal("show");
        },
        error: function () {
            messageSweet('error',"Error del Servidor!!","Ocurrio un error inesperado");
        }
    });
}