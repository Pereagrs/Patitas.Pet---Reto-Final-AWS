document.getElementById('registro-form').addEventListener('submit', function (e) {
  e.preventDefault();

  const nombre = document.getElementById('nombre').value;
  const correo = document.getElementById('email').value;
  const contrasena = document.getElementById('password').value;

  // Configuración de tu User Pool
  const poolData = {
    UserPoolId: 'us-east-1_0wumfD3lJ', // tu User Pool ID
    ClientId: '7c4ge9h84gsblv3ossvt75snio' // tu App Client ID
  };

  const userPool = new AmazonCognitoIdentity.CognitoUserPool(poolData);

  // Atributos del usuario
  const attributeList = [
    new AmazonCognitoIdentity.CognitoUserAttribute({ Name: 'name', Value: nombre }),
    new AmazonCognitoIdentity.CognitoUserAttribute({ Name: 'email', Value: correo })
  ];

  // Registro en Cognito
  userPool.signUp(correo, contrasena, attributeList, null, function (err, result) {
    if (err) {
      alert('❌ Error: ' + err.message || JSON.stringify(err));
      return;
    }

    alert('✅ Registro exitoso. Revisa tu email para confirmar la cuenta.');
    window.location.href = 'login.html';
  });
});
