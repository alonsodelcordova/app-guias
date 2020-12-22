function editarLink(id){
    $.ajax({
        url: "/api/link/"+id,
        method: 'GET',
        data: {},
        cache: false,
        dataType: 'json',
        success: function (respuesta) 
        {
            respuesta.forEach(provincia => {
                $("#id_provincia").append('<option value="'+provincia.id+'">'+provincia.nombre+'</option>');
            });
        },
        error: function () {
            messageSweet('error',"Error del Servidor!!","Ocurrio un error inesperado");
        }
    });
}
function eliminarLink(id){
    eliminarSweet("Eliminar link", "¿Realmente quiere salir?", "Eliminar", '/link/delete/id');
}