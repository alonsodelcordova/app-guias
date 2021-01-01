function editarMoneda(id){
    $.ajax({
        url: "/api/tipo-moneda/"+id,
        method: 'GET',
        data: {},
        cache: false,
        dataType: 'json',
        success: function (respuesta) 
        {
            $("#id").val(id);
            $("#exampleModalLabel").html("Actualizar Moneda");
            $("#nombre").val(respuesta.nombre);
            $("#prefijo").val(respuesta.prefijo);
            $("#modalMoneda").modal("show");
        },
        error: function () {
            messageSweet('error',"Error del Servidor!!","Ocurrio un error inesperado");
        }
    });
}
function eliminarMoneda(id){
    eliminarSweet("Eliminar Moneda!!", "¿Realmente quiere salir?", "Eliminar",id);
}

function eliminarDato(id){
    $.ajax({
        url: "../api/tipo-moneda/"+id,
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
