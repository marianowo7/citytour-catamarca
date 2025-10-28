document
  .getElementById("formulario")
  .addEventListener("submit", function (event) {
    event.preventDefault();
    if (validarFecha() && validarOrigenYDestino() && validarCantidad()) {
      alert("Datos del formulario son validos. Enviando formulario...");
    } else {
      alert("Por favor, corrija los errores en el formulario.");
    }
  });

function validarFecha() {
  const fechaForm = document.getElementById("fecha").value;
  const fechaActual = new Date();
  const fechaIngresada = new Date(fechaForm);

  if (fechaIngresada < fechaActual) {
    alert(
      "La fecha ingresada es anterior a la fecha actual. Por favor, ingrese una fecha válida."
    );
    return false;
  } else {
    return true;
  }
}

function validarOrigenYDestino() {
  const origen = document.getElementById("origen").value;
  const destino = document.getElementById("destino").value;

  if (origen === destino) {
    alert("El origen y el destino no pueden ser iguales.");
    return false;
  } else {
    return true;
  }
}

function validarCantidad() {
  const cantidad = document.getElementById("cantidad").value;

  if (cantidad <= 0 || cantidad > 50) {
    alert("La cantidad de pasajeros debe ser entre 1 y 50.");
    return false;
  } else {
    return true;
  }
}
