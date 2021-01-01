function editarVehiculo(id){
    $.ajax({
        url: "/api/vehiculo/"+id,
        method: 'GET',
        data: {},
        cache: false,
        dataType: 'json',
        success: function (respuesta) 
        {
            $("#id").val(id);
            $("#exampleModalLabel").html("Actualizar vehiculo");
            $("#modelo_vehiculo").val(respuesta.modelo_vehiculo);
            $("#marca_vehiculo").val(respuesta.marca_vehiculo);
            $("#placa_vehiculo").val(respuesta.placa_vehiculo);
            $("#modalVehiculo").modal("show");
        },
        error: function () {
            messageSweet('error',"Error del Servidor!!","Ocurrio un error inesperado");
        }
    });
}
function eliminarVehiculo(id){
    eliminarSweet("Eliminar vehiculo!!", "¿Realmente quiere salir?", "Eliminar",id);
}

function eliminarDato(id){
    $.ajax({
        url: "/api/vehiculo/"+id,
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
