function editarFactura(id){
    $.ajax({
        url: "/api/factura/"+id,
        method: 'GET',
        data: {},
        cache: false,
        dataType: 'json',
        success: function (respuesta) 
        {
            $("#id").val(id);
            $("#exampleModalLabel").html("Actualizar factura");
            $("#numero_factura").val(respuesta.numero_factura);
            $("#fecha_emision").val(respuesta.fecha_emision);
            $("#total").val(respuesta.total);
            $("#id_cliente option[value="+ respuesta.id_cliente +"]").attr("selected",true);
            $("#id_tipo_moneda option[value="+ respuesta.id_tipo_moneda +"]").attr("selected",true);

            $("#observacion").html(respuesta.observacion);
            $("#modalFactura").modal("show");
        },
        error: function () {
            messageSweet('error',"Error del Servidor!!","Ocurrio un error inesperado");
        }
    });
}
function eliminarFactura(id){
    eliminarSweet("Eliminar factura!!", "¿Realmente quiere salir?", "Eliminar",id);
}

function eliminarDato(id){
    $.ajax({
        url: "/api/factura/"+id,
        method: 'DELETE',
        data: $("#form").serialize(),
        cache: false,
        dataType: 'json',
        success: function (data) {
            messageSweet('success',data.mesage,"Se eliminó con exito");
            window.location.reload();
        },
        error: function (data) {
            messageSweet('error',"Error del Servidor!!","Ocurrio un error inesperado");
        }
    });
}
