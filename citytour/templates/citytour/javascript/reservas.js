const formulario = document.getElementById("miformulario");

formulario.addEventListener("submit", (event) => {
  event.preventDefault();
  if (validarFormulario()) {
    alert("Formulario enviado correctamente");
    formulario.submit();
  }
});

function validarFormulario() {
  let esvalido = true;

  const fechaForm = document.getElementById("fecha").value;
  const fechaActual = new Date();
  const fechaIngresada = new Date(fechaForm);
  const errorFecha = document.getElementById("errorfecha");

  const nombre = document.getElementById("nombre").value;
  const errorNombre = document.getElementById("errornombre");
  const nombreWords = nombre.split(/\s+/);

  const apellido = document.getElementById("apellido").value;
  const errorApellido = document.getElementById("errorapellido");
  const apellidoWords = apellido.split(/\s+/);

  if (fechaIngresada < fechaActual) {
    errorFecha.textContent =
      "La fecha ingresada es anterior a la fecha actual. Por favor, ingrese una fecha válida.";
    esvalido = false;
  } else {
    errorFecha.textContent = "";
  }
  if (nombreWords.length > 4) {
    errorNombre.textContent = "El nombre no puede contener más de 4 palabras";
    esvalido = false;
  } else {
    errorNombre.textContent = "";
  }
  if (apellidoWords.length > 4) {
    errorApellido.textContent =
      "El apellido no puede contener más de 4 palabras";
    esvalido = false;
  } else {
    errorApellido.textContent = "";
  }

  return esvalido;
}
