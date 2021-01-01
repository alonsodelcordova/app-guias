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

