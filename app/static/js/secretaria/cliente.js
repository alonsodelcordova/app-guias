function editarCliente(id){
    $.ajax({
        url: "/api/cliente/"+id,
        method: 'GET',
        data: {},
        cache: false,
        dataType: 'json',
        success: function (respuesta) 
        {
            $("#id").val(id);
            $("#exampleModalLabel").html("Actualizar cliente");
            $("#razon_social").val(respuesta.razon_social);
            $("#numero_documento").val(respuesta.numero_documento);
            $("#direccion").val(respuesta.direccion);
            $("#tipo_documento option[value="+ respuesta.tipo_documento +"]").attr("selected",true);
            $("#modalCliente").modal("show");
        },
        error: function () {
            messageSweet('error',"Error del Servidor!!","Ocurrio un error inesperado");
        }
    });
}
function eliminarCliente(id){
    eliminarSweet("Eliminar cliente!!", "¿Realmente quiere salir?", "Eliminar",id);
}

function eliminarDato(id){
    $.ajax({
        url: "/api/cliente/"+id,
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
