const AWS = require('aws-sdk');
const cognito = new AWS.CognitoIdentityServiceProvider();
const dynamodb = new AWS.DynamoDB.DocumentClient();

exports.handler = async (event) => {
  if (event.triggerSource === 'PostConfirmation_ConfirmSignUp') {
    // Añadir al grupo Cognito
    await cognito.adminAddUserToGroup({
      UserPoolId: 'us-east-1_0wumfD3lJ',
      Username: event.userName,
      GroupName: 'PatitasPetUsers'
    }).promise();

    // Guardar datos en DynamoDB
    const userAttributes = event.request.userAttributes;

    const protectora = {
      protectora_id: userAttributes.sub,
      nombre: userAttributes['custom:nombre'] || 'Sin nombre',
      email: userAttributes.email,
      telefono: userAttributes['custom:telefono'] || '',
      ubicacion: userAttributes['custom:ubicacion'] || '',
      fechaRegistro: new Date().toISOString()
    };

    const params = {
      TableName: 'Protectoras',
      Item: protectora
    };

    try {
      await dynamodb.put(params).promise();
      console.log('✅ Protectora guardada en DynamoDB');
    } catch (error) {
      console.error('❌ Error guardando protectora:', error);
      throw error;
    }
  }

  return event;
};
