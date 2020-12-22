ocultar();
function ocultar(){
    $("#id_distrito option").hide();
    $("#id_provincia option").hide();
}

function mostrarProvincias(){
    ocultar();
    var id = $("#id_departamento").val();
    $.ajax({
        url: "/api/provincias/"+id,
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

function mostrarDistritos(){
    $("#id_distrito option").hide();
    var id = $("#id_provincia").val();
    $.ajax({
        url: "/api/distritos/"+id,
        method: 'GET',
        data: {},
        cache: false,
        dataType: 'json',
        success: function (respuesta) 
        {
            respuesta.forEach(distrito => {
                $("#id_distrito").append('<option value="'+distrito.id+'">'+distrito.nombre+'</option>');
            });
        },
        error: function () {
            messageSweet('error',"Error del Servidor!!","Ocurrio un error inesperado");
        }
    });
}