function agregarUsuario(){
    $("#exampleModalLabel").html("Agregar Usuario");  
    $("#modalUsuario").modal("show");
    $("#password").show();
    $("#password2").show();
    $("#form").trigger("reset");

}

function editarUsuario(id){
    $('#id').val(id);
    $.ajax({
        url: "/api/usuario/"+id,
        method: 'GET',
        data: {},
        cache: false,
        dataType: 'json',
        success: function (respuesta) 
        {
            $('#id').val(id);
            $("#id_cargo option[value="+ respuesta.id_cargo +"]").attr("selected",true);
            $("#id_oficina option[value="+ respuesta.id_oficina +"]").attr("selected",true);
            $("#usuario").val(respuesta.usuario);
            $("#dni").val(respuesta.dni);
            $("#password").hide();
            $("#password2").hide();
            //para el modal
            $("#exampleModalLabel").html("Actualizar Usuario");  
            $("#modalUsuario").modal("show");
        },
        error: function () {
            messageSweet('error',"Error del Servidor!!","Ocurrio un error inesperado");
        }
    });
}



function eliminarUsuario(id){
    eliminarSweet("Eliminar Usuario!!", "¿Realmente quiere salir?", "Eliminar",id);
}

function eliminarDato(id){
    $.ajax({
        url: "/api/usuario/"+id,
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