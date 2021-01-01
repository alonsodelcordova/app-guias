ocultar();
function ocultar(){
    $("#id_distrito option").hide();
    $("#id_provincia option").hide();
    $("#id_distrito").val("0");
    $("#id_provincia").val("0");
}

function mostrarProvincias(id_provincia=0){
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
            $("#id_provincia option").attr("selected",false);
            respuesta.forEach(provincia => {
                $("#id_provincia").append('<option value="'+provincia.id+'">'+provincia.nombre+'</option>');
            });
            if(id_provincia!=0){
                $("#id_provincia option[value="+ id_provincia +"]").attr("selected",true);
            }
        },
        error: function () {
            messageSweet('error',"Error del Servidor!!","Ocurrio un error inesperado");
        }
    });
}

function mostrarDistritos(id_provincia=0,id_distrito=0){
    $("#id_distrito option").hide();
    $("#id_distrito").val("0");
    let id = 0;
    if(id_provincia!=0){
        id=id_provincia;
    }else{
        id = $("#id_provincia").val();
    }
    
    $.ajax({
        url: "/api/distritos/"+id,
        method: 'GET',
        data: {},
        cache: false,
        dataType: 'json',
        success: function (respuesta) 
        {
            $("#id_distrito option").attr("selected",false);
            respuesta.forEach(distrito => {
                $("#id_distrito").append('<option value="'+distrito.id+'">'+distrito.nombre+'</option>');
            });
            if(id_distrito!=0){
                $("#id_distrito option[value="+ id_distrito +"]").attr("selected",true);
            }
        },
        error: function () {
            messageSweet('error',"Error del Servidor!!","Ocurrio un error inesperado");
        }
    });
}