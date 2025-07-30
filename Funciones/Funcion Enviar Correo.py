import boto3
import json

ses = boto3.client('ses', region_name='us-east-1')  # Asegúrate de usar la región de SES

def lambda_handler(event, context):
    try:
        data = json.loads(event['body'])

        nombre = data['nombre']
        email = data['email']
        mensaje = data['mensaje']
        animal = data['animal']

        response = ses.send_email(
            Source='info@patitas.pet',  # Dirección verificada en SES
            Destination={
                'ToAddresses': ['protectora@ejemplo.com']  # Cambia por quien reciba el correo
            },
            Message={
                'Subject': {
                    'Data': f'Consulta sobre {animal}'
                },
                'Body': {
                    'Text': {
                        'Data': f'Nombre: {nombre}\nEmail: {email}\nMensaje: {mensaje}'
                    }
                }
            }
        )

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Correo enviado correctamente'})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
