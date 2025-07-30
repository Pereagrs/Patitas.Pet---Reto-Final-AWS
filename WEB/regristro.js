document.getElementById('registro-form').addEventListener('submit', async function (e) {
  e.preventDefault();

  // Captura valores del formulario
  const nombre = document.getElementById('nombre').value;
  const correo = document.getElementById('email').value;
  const contrasena = document.getElementById('password').value;

  const formData = new FormData();
  formData.append('nombre', nombre);
  formData.append('email', correo);
  formData.append('password', contrasena);

  try {
    const response = await fetch('/registro', {
      method: 'POST',
      body: formData
    });

    const resultado = await response.json();
    if (response.ok) {
      alert('✅ ' + resultado.mensaje);
      window.location.href = 'login.html';
    } else {
      alert('❌ ' + resultado.error);
    }
  } catch (error) {
    alert('💥 Error de red: ' + error.message);
  }
});
