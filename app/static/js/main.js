$(document).ready(function () {
    window.setTimeout(function () {
        $("#success-alert").alert('close');
    }, 3000);
});

window.onload = function(){
    $("#pre-loader").fadeOut();
}

function messageSweet(icon, title, text) {
    Swal.fire({
        icon: icon,
        title: title,
        text: text
    });
}
function cargando(titulo){
    Swal.fire({
      title: titulo,
      html: 'Espere un momento por favor...',
      timerProgressBar: true,
      didOpen: () => {
        Swal.showLoading()
      }
    });
}
function eliminarSweet(title, message, btn_msg,id) {
    Swal.fire({
        title: title,
        text: message,
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        cancelButtonText: 'Cancelar',
        confirmButtonText: btn_msg
    }).then((result) => {
        if (result.isConfirmed) {
            eliminarDato(id);
        }
    })
}
function abrirModal(nombre,titulo) {
    limpiarDatos();
    $("#id").val("");
    $("#exampleModalLabel").html(titulo);
    $("#" + nombre).modal("show");
}
function limpiarDatos(){
    $("#form")[0].reset();
}

function addUser(elem) {
    elem.preventDefault();
    if ($("#password").val() == $("#password2").val()) {
        elem.target.submit();
    } else {
        messageSweet('error', 'Las contraseñas no coinciden!!', 'ingrese contraseñas iguales')
        $("#password").focus();
    }
}

function cerrar_session() {
    Swal.fire({
        title: "Cerrar Sesion",
        text: "¿Estás seguro de cerrar session?",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        cancelButtonText: 'Cancelar',
        confirmButtonText: 'Cerrar Session'
    }).then((result) => {
        if (result.isConfirmed) {
            window.location = "/logout"
        }
    })
}

function imprimir(id) {

    var element = document.getElementById('div-imprimir');
    var opt = {
        margin: 0.2,

        filename: 'guia-remision-00' + id + '.pdf',
        image: { type: 'jpeg', quality: 0.98 },
        html2canvas: { scale: 2 },
        jsPDF: { unit: 'in', format: 'letter', orientation: 'landscape' }
    };
    // New Promise-based usage:
    html2pdf().set(opt).from(element).save();
}

function buscarTabla(){
    var tableReg = document.getElementById('tableData');
    var searchText = $('#datoBuscar').val().toLowerCase();
    for (var i = 1; i < tableReg.rows.length; i++) {
        var cellsOfRow = tableReg.rows[i].getElementsByTagName('td');
        var found = false;
        for (var j = 0; j < cellsOfRow.length && !found; j++) {
            var compareWith = cellsOfRow[j].innerHTML.toLowerCase();
            if (searchText.length == 0 || (compareWith.indexOf(searchText) > -1)) {
                found = true;
            }
        }
        if (found) {
            tableReg.rows[i].style.display = '';
        } else {
            tableReg.rows[i].style.display = 'none';
        }
    }
  }

  function back(){
    history.back();
  }