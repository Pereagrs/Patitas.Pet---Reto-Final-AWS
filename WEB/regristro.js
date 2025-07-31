document.getElementById('registro-form').addEventListener('submit', function (e) {
  e.preventDefault();

  const nombre = document.getElementById('nombre').value;
  const correo = document.getElementById('email').value;
  const contrasena = document.getElementById('password').value;

  // Configuración del User Pool de Cognito
  const poolData = {
    UserPoolId: 'us-east-1_0wumfD3lJ', // tu User Pool ID
    ClientId: '7c4ge9h84gsblv3ossvt75snio' // tu App Client ID
  };

  const userPool = new AmazonCognitoIdentity.CognitoUserPool(poolData);

  // Lista de atributos
  const attributeList = [
    // Atributo estándar
    new AmazonCognitoIdentity.CognitoUserAttribute({ Name: 'email', Value: correo }),

    // Atributo personalizado (asegúrate que existe en tu User Pool)
    new AmazonCognitoIdentity.CognitoUserAttribute({ Name: 'custom:nombre', Value: nombre })
  ];

  // Registro en Cognito
  userPool.signUp(correo, contrasena, attributeList, null, function (err, result) {
    if (err) {
      alert('❌ Error: ' + (err.message || JSON.stringify(err)));
      return;
    }

    alert('✅ Registro exitoso. Revisa tu email para confirmar la cuenta.');
    window.location.href = 'login.html';
  });
});
