const AWS = require('aws-sdk');
const cognito = new AWS.CognitoIdentityServiceProvider();

exports.handler = async (event) => {
  if (event.triggerSource === 'PostConfirmation_ConfirmSignUp') {
    await cognito.adminAddUserToGroup({
      UserPoolId: us-east-1_0wumfD3lJ,
      Username: event.userName,
      GroupName: 'PatitasPetUsers'
    }).promise();
  }
  return event;
};