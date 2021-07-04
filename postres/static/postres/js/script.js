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
    $.get("https://apis.digital.gob.cl/fl/feriados/" + yyyy + "/" + mm, function(data) {
        $.each(data, function(i, item) {
            $('#feriados').append("<tr><td>" + (i + 1) + "</td><td>" + item.nombre + "</td><td>" +
                item.fecha + "</td><td>" + item.tipo + "</td></tr>");
        });
    });
});


//alertas
$(document).on('click', '.eliminar', function() {
    return confirm('¿Esta seguro que desea eliminar este producto?');
})

function alerta() {
    alert('No disponible 😔');
}


//Consumo de Propia API
$(document).ready(function() {
    //para setear los Header de la llamada a la API y otrgarle permisos
    $.ajaxSetup({
        headers: {
            'Authorization': 'Token 971342ba762348598d5a8203cadd66e889d177b9'
<<<<<<< HEAD
=======

>>>>>>> isabella
        }
    });
    //obtengo la info de la API
    $.getJSON("http://127.0.0.1:8000/api/categoria-producto", function(json) {
        $.each(json, function(i, item) {
            $('#propia-api').append("<tr><td>" + item.ID_CATPROD + "</td><td>" +
                item.NOM_CATPROD + "</td></tr>");
        });
    }).fail(function() {
        console.log('Error al consumir la API!');
    });
});

//POST a la API para obtener el token 
function log(username, password) {
    console.log(username, password)
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "text/plain");

    var raw = JSON.stringify({
        "username": username,
        "password": password
    });

    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
    };

    fetch("http://127.0.0.1:8000/api/login", requestOptions)
        .then(response => response.text())
        .then(result => { console.log(result) })
}