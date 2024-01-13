function editarOficina(id){
    $.ajax({
        url: "/api/oficina/"+id,
        method: 'GET',
        data: {},
        cache: false,
        dataType: 'json',
        success: function (respuesta) 
        {
            $('#id').val(id);
            $("#nombre").val(respuesta.nombre);
            $("#direccion").val(respuesta.direccion);
            //para la direccion
            $("#exampleModalLabel").html("Actualizar Oficina");  
            $("#modalOficina").modal("show");
            
        },
        error: function () {
            messageSweet('error',"Error del Servidor!!","Ocurrio un error inesperado");
        }
    });
}
function eliminarOficina(id){
    eliminarSweet("Eliminar Oficina!!", "¿Realmente quiere salir?", "Eliminar",id);
}

function eliminarDato(id){
    $.ajax({
        url: "/api/oficina/"+id,
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