function editarPersona(id){
    $.ajax({
        url: "/api/persona/"+id,
        method: 'GET',
        data: {},
        cache: false,
        dataType: 'json',
        success: function (respuesta) 
        {
            $('#id').val(id);
            $("#nombres").val(respuesta.nombres);
            $("#dni").val(respuesta.dni);
            $("#primer_apellido").val(respuesta.primer_apellido);
            $("#segundo_apellido").val(respuesta.segundo_apellido);
            $("#email").val(respuesta.email);
            $("#numero_celular").val(respuesta.numero_celular);
            //$("#dni").val(respuesta.dni);
            //$("#dni").val(respuesta.dni);
            $("#estado_civil option[value="+ respuesta.estado_civil +"]").attr("selected",true);
            $("#sexo option[value="+ respuesta.sexo +"]").attr("selected",true);

            //para la direccion
            $("#direccion").val(respuesta.direccion);
            $("#id_departamento option").attr("selected",false);
            $("#id_departamento option[value="+ respuesta.id_departamento +"]").attr("selected",true);
            mostrarProvincias(respuesta.id_provincia);
            mostrarDistritos(respuesta.id_provincia,respuesta.id_distrito);

            //para el modal
            $("#exampleModalLabel").html("Actualizar Persona");  
            $("#modalPersona").modal("show");
            
        },
        error: function () {
            messageSweet('error',"Error del Servidor!!","Ocurrio un error inesperado");
        }
    });
}
function eliminarPersona(id){
    eliminarSweet("Eliminar Persona!!", "¿Realmente quiere salir?", "Eliminar",id);
}

function eliminarDato(id){
    $.ajax({
        url: "/api/persona/"+id,
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