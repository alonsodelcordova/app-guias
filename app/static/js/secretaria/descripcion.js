function editarDescripcion(id){
    $.ajax({
        url: "/api/descripcion-guia/"+id,
        method: 'GET',
        data: {},
        cache: false,
        dataType: 'json',
        success: function (respuesta) 
        {
            $("#id").val(id);
            $("#exampleModalLabel").html("Actualizar Descripcion");
            $("#cantidad").val(respuesta.cantidad);
            $("#unidad_medida").val(respuesta.unidad_medida);
            $("#descripcion").val(respuesta.descripcion);
            $("#modalDescripcion").modal("show");
        },
        error: function () {
            messageSweet('error',"Error del Servidor!!","Ocurrio un error inesperado");
        }
    });
}
function eliminarDescripcion(id){
    eliminarSweet("Eliminar Descripcion de Guia!!", "¿Realmente quiere salir?", "Eliminar",id);
}

function eliminarDato(id){
    $.ajax({
        url: "/api/descripcion-guia/"+id,
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
