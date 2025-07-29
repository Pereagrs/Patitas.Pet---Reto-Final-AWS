// Referencia los campos del formulario
document.getElementById('signupForm').addEventListener('submit', function (e) {
  e.preventDefault(); // Evita que se recargue la página

  // Recupera valores del formulario
  const nombre = document.getElementById('nombre').value;
  const correo = document.getElementById('correo').value;
  const contrasena = document.getElementById('contrasena').value;

  // Configuración del User Pool
  const poolData = {
    UserPoolId: 'us-east-1_0wumfD3lJ', // ← tu UserPoolId
    ClientId: '7c4ge9h84gsblv3ossvt75snio' // ← tu ClientId
  };

  const userPool = new AmazonCognitoIdentity.CognitoUserPool(poolData);

  // Atributos personalizados del usuario
  const attributeList = [];

  const dataEmail = {
    Name: 'email',
    Value: correo
  };
  const dataNombre = {
    Name: 'name',
    Value: nombre
  };

  const atributoEmail = new AmazonCognitoIdentity.CognitoUserAttribute(dataEmail);
  const atributoNombre = new AmazonCognitoIdentity.CognitoUserAttribute(dataNombre);

  attributeList.push(atributoEmail);
  attributeList.push(atributoNombre);

  // Registrar usuario en Cognito
  userPool.signUp(correo, contrasena, attributeList, null, function (err, result) {
    if (err) {
      alert('❌ Error: ' + err.message || JSON.stringify(err));
      return;
    }

    const cognitoUser = result.user;
    alert('✅ Registro exitoso. Usuario: ' + cognitoUser.getUsername());
  });
});
