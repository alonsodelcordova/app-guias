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
            console.log("depa:"+respuesta.id_departamento);
            console.log("dist:"+respuesta.id_distrito);
            $("#id_departamento option").attr("selected",false);
            $("#id_departamento option[value="+ respuesta.id_departamento +"]").attr("selected",true);
            mostrarProvincias(respuesta.id_provincia);
            $("#exampleModalLabel").html("Actualizar Oficina");  
            $("#modalOficina").modal("show");
            mostrarDistritos(respuesta.id_provincia,respuesta.id_distrito);
            
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