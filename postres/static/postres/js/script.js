$(document).ready(function() {
    $("#formularioContacto").validate({
        rules: {
            nombre: {
                required: true,
                minlength: 3
            },
            apellido: {
                required: true,
                minlength: 3
            },
            correo: {
                required: true,
                email: true
            },
            telefono: {
                required: true,
                number: true,
                minlength: 9,
                maxlength: 9
            },
            mensaje: {
                required: true,
                minlength: 10,
                maxlength: 150
            }

        },
        messages: {
            nombre: {
                required: "Debe ingresar su nombre",
                minlength: "El nombre debe tener mínimo 3 carácteres"
            },
            apellido: {
                required: "Debe ingresar su apellido",
                minlength: "El apellido debe tener mínimo 3 carácteres"
            },
            correo: {
                required: "Debe ingresar su correo electrónico",
                email: "El email debe tener un formato válido"
            },
            telefono: {
                required: "Debe ingresar su teléfono",
                number: "Debe ingresar sólo números",
                minlength: "El teléfono debe tener 9 dígitos",
                maxlength: "El teléfono debe tener 9 dígitos"
            },
            mensaje: {
                required: "Debe ingresar un mensaje",
                minlength: "El mensaje debe tener mínimo 10 carácteres",
                maxlength: "El mensaje no debe tener mas de 150 carácteres"
            }
        }

    });

});

//Llamada a API Ferias Chile
$(document).ready(function() {
    var today = new Date();
    var mm = today.getMonth() + 1;
    var yyyy = today.getFullYear();
    $.get("https://apis.digital.gob.cl/fl/feriados/"+yyyy+"/"+mm, function(data) {
        $.each(data, function(i, item) {
            $('#feriados').append("<tr><td>" + (i+1) + "</td><td>" + item.nombre + "</td><td>" +
            item.fecha + "</td><td>" + item.tipo + "</td></tr>");
        });
    });
});


//alertas
$(document).on('click', '.eliminar', function(){
    return confirm('¿Esta seguro que desea eliminar este producto?');
})

function alerta() {
    alert('No disponible 😔');
}
