function editarTransportista(id){
    $.ajax({
        url: "/api/transportista/"+id,
        method: 'GET',
        data: {},
        cache: false,
        dataType: 'json',
        success: function (respuesta) 
        {
            $("#id").val(id);
            $("#exampleModalLabel").html("Actualizar transportista");
            $("#ruc").val(respuesta.ruc);
            $("#numero_licencia").val(respuesta.numero_licencia);
            $("#denominacion").val(respuesta.denominacion);
            $("#nombres").val(respuesta.nombres);
            $("#apellidos").val(respuesta.apellidos);
            $("#modalTransportista").modal("show");
        },
        error: function () {
            messageSweet('error',"Error del Servidor!!","Ocurrio un error inesperado");
        }
    });
}
function eliminarTransportista(id){
    eliminarSweet("Eliminar transportista!!", "¿Realmente quiere salir?", "Eliminar",id);
}

function eliminarDato(id){
    $.ajax({
        url: "/api/transportista/"+id,
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
