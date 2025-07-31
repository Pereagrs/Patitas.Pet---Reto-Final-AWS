const AWS = require('aws-sdk');
const ses = new AWS.SES();
const cognito = new AWS.CognitoIdentityServiceProvider();

exports.handler = async (event) => {
  try {
    const datos = JSON.parse(event.body);
    const { nombre, telefono, email, mensaje, protectoraId } = datos;

    // 1. Buscar email de la protectora
    const user = await cognito.adminGetUser({
      UserPoolId: 'TU_USER_POOL_ID',
      Username: protectoraId
    }).promise();

    const emailAttr = user.UserAttributes.find(attr => attr.Name === 'email');
    const destinatario = emailAttr?.Value;

    if (!destinatario) throw new Error('No se encontró el email');

    // 2. Enviar correo
    await ses.sendEmail({
      Source: 'noreply@patitas.pet',
      Destination: { ToAddresses: [destinatario] },
      Message: {
        Subject: { Data: 'Nueva solicitud de adopción 🐾' },
        Body: {
          Text: {
            Data: `Nombre: ${nombre}\nTeléfono: ${telefono}\nEmail: ${email}\n\nMensaje:\n${mensaje}`
          }
        }
      }
    }).promise();

    return {
      statusCode: 200,
      body: JSON.stringify({ mensaje: 'Correo enviado con éxito' })
    };

  } catch (error) {
    console.error('Error:', error);
    return {
      statusCode: 500,
      body: JSON.stringify({ error: 'Hubo un problema al enviar el correo' })
    };
  }
};
