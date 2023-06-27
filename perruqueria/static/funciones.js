let formulario = document.getElementById('formulario');
let nom_cliente = document.getElementById('nombre_cliente');
let nom_mascota = document.getElementById('nombre_mascota');
let email = document.getElementById('email');
let telefono = document.getElementById('telefono');
let fecha = document.getElementById('fecha');
let hora = document.getElementById('hora');
let raza = document.getElementById('raza');


nom_cliente.addEventListener("input", validarNombre);

nom_mascota.addEventListener("input", validarNombreMascota);
email.addEventListener("input", validarEmail);
telefono.addEventListener("input", validarTelefono);
fecha.addEventListener("input", validarFecha);
hora.addEventListener("input", validarHora)
raza.addEventListener("input", validarRaza);


function validarNombre() {
  let nombreValor = nom_cliente.value.trim();
  let errorNombre = document.getElementById("errorNombre");
  errorNombre.textContent = "";
  errorNombre.className = "";

  if (nombreValor.length < 2 || nombreValor.length > 20) {
    errorNombre.textContent = "El nombre debe tener entre 2 y 20 caracteres.";
    errorNombre.className = "error";
  }
}
function validarNombreMascota() {
    let nombreMValor = nom_mascota.value.trim();
    let errorNombreMascota = document.getElementById("errorNombreMascota");
    errorNombreMascota.textContent = "";
    errorNombreMascota.className = "";

    if (nombreMValor.length < 2 || nombreMValor.length > 20) {
      errorNombreMascota.textContent = "El nombre debe tener entre 2 y 20 caracteres.";
      errorNombreMascota.className = "error";
    }
  }
function validarEmail(){
  let emailcli = email.value.trim();
  let errorEmail = document.getElementById("errorEmail");
  errorEmail.textContent = "";
  errorEmail.className = "";

  let emailRegex = /^\S+@\S+\.\S+$/;

  if(!emailRegex.test(emailcli)){
    errorEmail.textContent = "El correo electronico no es válido";
    errorEmail.className = "error";
  }
}

function validarTelefono() {
  let telefonoValor = telefono.value.trim();
  let errorTelefono = document.getElementById("errorTelefono");
  errorTelefono.textContent = "";
  errorTelefono.className = "";

  let telefonoRegex = /^\d{9}$/;

  if (!telefonoRegex.test(telefonoValor)) {
    errorTelefono.textContent = "Por favor ingrese un número de teléfono válido.";
    errorTelefono.className = "error";
  }
}

function validarFecha() {
  let fechaValor = fecha.value.trim();
  let errorFecha = document.getElementById("errorFecha");
  errorFecha.textContent = "";
  errorFecha.className = "";

  let fechaRegex = /^\d{4}-\d{2}-\d{2}$/;

  if (!fechaRegex.test(fechaValor)) {
    errorFecha.textContent = "Por favor ingrese una fecha válida.";
    errorFecha.className = "error";
  }
}

function validarHora() {
  let horaValor = hora.value.trim();
  let errorHora = document.getElementById("errorHora");
  errorHora.textContent = "";
  errorHora.className = "";

  let horaRegex = /^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$/;

  if (!horaRegex.test(horaValor)) {
    errorHora.textContent = "Por favor ingrese una hora válida.";
    errorHora.className = "error";

  }
}
function validarRaza() {
    let tipo = raza.value.trim();
    let errorRaza = document.getElementById("errorRaza");
    errorRaza.textContent = "";
    errorRaza.className = "";


    if (tipo.length < 2 || tipo.length > 20) {
      errorRaza.textContent = "El nombre debe tener entre 2 y 20 caracteres.";
      errorRaza.className = "error";

    }
  }

function enviarFormulario() {
  validarNombre();
  validarNombreMascota();
  validarEmail();
  validarTelefono();
  validarFecha();
  validarHora();
  validarRaza();

  let errores = document.querySelectorAll(".error");
  let camposVacios = document.querySelectorAll("input:required:invalid");
  
  if (errores.length > 0 || camposVacios.length > 0) {
    event.preventDefault();
    alert("Por favor, complete todos los campos antes de enviar el formulario.");
  }
} 

// formulario.addEventListener("submit", enviarFormulario);


// Obtener referencia al elemento select de la hora
var selectHora = document.getElementById("hora");

// Generar las opciones de hora
for (var i = 9; i <= 17; i++) {
    var option = document.createElement("option");
    option.value = i.toString().padStart(2, "0") + ":00"; // Formato hh:mm
    option.text = i.toString().padStart(2, "0") + ":00";
    selectHora.appendChild(option);}