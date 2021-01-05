function editarPregunta(id){
    $.ajax({
        url: "/api/pregunta/"+id,
        method: 'GET',
        data: {},
        cache: false,
        dataType: 'json',
        success: function (respuesta) 
        {
            $('#id').val(id);
            $("#pregunta").val(respuesta.pregunta);
            $("#respuesta").val(respuesta.respuesta);
            $("#id_usuario option[value="+ respuesta.id_usuario +"]").attr("selected",true);
            $("#exampleModalLabel").html("Actualizar Pregunta");  
            $("#modalPregunta").modal("show");
            
        },
        error: function () {
            messageSweet('error',"Error del Servidor!!","Ocurrio un error inesperado");
        }
    });
}
function eliminarPregunta(id){
    eliminarSweet("Eliminar pregunta!!", "¿Realmente quiere salir?", "Eliminar",id);
}

function eliminarDato(id){
    $.ajax({
        url: "/api/pregunta/"+id,
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