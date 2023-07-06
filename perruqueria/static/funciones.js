let formulario = document.getElementById('formulario');
let username = document.getElementById('id_username');
let password = document.getElementById('id_password');
let passwordConfirmation = document.getElementById('id_password_confirmation');
let nombre = document.getElementById('nombre_cliente');
let apellido = document.getElementById('id_apellido');
let telefono = document.getElementById('telefono');
let email = document.getElementById('email');

function validarUsername() {
  let usernameValor = username.value.trim();
  let errorUsername = document.getElementById("errorUsername");
  errorUsername.textContent = "";
  errorUsername.className = "";

  if (usernameValor.length < 2 || usernameValor.length > 150) {
    errorUsername.textContent = "El username debe tener entre 2 y 150 caracteres.";
    errorUsername.className = "error";
  }
}

function validarPassword() {
  let passwordValor = password.value.trim();
  let errorPassword = document.getElementById("errorPassword");
  errorPassword.textContent = "";
  errorPassword.className = "";

  if (passwordValor.length < 8) {
    errorPassword.textContent = "La contraseña debe tener al menos 8 caracteres.";
    errorPassword.className = "error";
  }
}

function validarPasswordConfirmation() {
  let passwordValor = password.value.trim();
  let passwordConfirmationValor = passwordConfirmation.value.trim();
  let errorPasswordConfirmation = document.getElementById("errorPasswordConfirmation");
  errorPasswordConfirmation.textContent = "";
  errorPasswordConfirmation.className = "";

  if (passwordConfirmationValor !== passwordValor) {
    errorPasswordConfirmation.textContent = "Las contraseñas no coinciden.";
    errorPasswordConfirmation.className = "error";
  }
  else if (passwordConfirmationValor < 8){
    errorPasswordConfirmation.textContent = "La contraseña debe tener al menos 8 caracteres.";
    errorPasswordConfirmation.className = "error";
  }
}

function validarNombre() {
  let nombreValor = nombre.value.trim();
  let errorNombre = document.getElementById("errorNombre");
  errorNombre.textContent = "";
  errorNombre.className = "";

  if (nombreValor.length < 2 || nombreValor.length > 30) {
    errorNombre.textContent = "El nombre debe tener entre 2 y 30 caracteres.";
    errorNombre.className = "error";
  }
}

function validarApellido() {
  let apellidoValor = apellido.value.trim();
  let errorApellido = document.getElementById("errorApellido");
  errorApellido.textContent = "";
  errorApellido.className = "";

  if (apellidoValor.length < 2 || apellidoValor.length > 30) {
    errorApellido.textContent = "El apellido debe tener entre 2 y 30 caracteres.";
    errorApellido.className = "error";
  }
}

function validarTelefono() {
  let telefonoValor = telefono.value.trim();
  let errorTelefono = document.getElementById("errorTelefono");
  errorTelefono.textContent = "";
  errorTelefono.className = "";

  let telefonoRegex = /^\d{9}$/;

  if (!telefonoRegex.test(telefonoValor)) {
    errorTelefono.textContent = "Por favor, ingrese un número de teléfono válido.";
    errorTelefono.className = "error";
  }
}

function validarEmail() {
  let emailValor = email.value.trim();
  let errorEmail = document.getElementById("errorEmail");
  errorEmail.textContent = "";
  errorEmail.className = "";
  let emailRegex = /^\S+@\S+\.\S+$/;

  if (!emailRegex.test(emailValor)) {
    errorEmail.textContent = "Por favor, ingrese un correo electrónico válido.";
    errorEmail.className = "error";
  }
}

function enviarFormulario() {
  validarUsername();
  validarPassword();
  validarPasswordConfirmation();
  validarNombre();
  validarApellido();
  validarTelefono();
  validarEmail();

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