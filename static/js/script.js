$(document).ready(function() {
  $('#login-form').submit(function(e) {
    e.preventDefault(); // Evita que se recargue la página al enviar el formulario
    var username = $('#username').val().trim();
    var password = $('#password').val().trim();
    // Validaciones
    if (username === '') {
      $('#username-error').text('Ingrese su nombre de usuario');
      return false; // Si el campo de usuario está vacío, no se envía el formulario
    } else if (username.length < 3) {
      $('#username-error').text('El usuario debe tener al menos 3 caracteres');
      return false; // Si el usuario tiene menos de 3 caracteres, no se envía el formulario
    } else {
      $('#username-error').empty(); // Si el usuario es válido, se limpia el mensaje de error
    }

    if (password === '') {
      $('#password-error').text('Ingrese su contraseña');
      return false; // Si el campo de contraseña está vacío, no se envía el formulario
    } else if (password.length < 6) {
      $('#password-error').text('La contraseña debe tener al menos 6 caracteres');
      return false; // Si la contraseña tiene menos de 6 caracteres, no se envía el formulario
    } else {
      $('#password-error').empty(); // Si la contraseña es válida, se limpia el mensaje de error
    }

    // Aquí puedes agregar tu código para enviar el formulario
  });
});