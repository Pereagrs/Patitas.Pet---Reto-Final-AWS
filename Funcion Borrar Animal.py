import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Animales')

def lambda_handler(event, context):
    try:
        # 1. Parsear el cuerpo recibido en formato JSON
        body = json.loads(event['body'])

        protectora_id = body.get('protectora_id')
        animal_id = body.get('animal_id')

        # 2. Validar campos obligatorios
        if not protectora_id or not animal_id:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Faltan datos obligatorios: protectora_id o animal_id.'})
            }

        # 3. Eliminar el item
        table.delete_item(
            Key={
                'protectora_id': protectora_id,
                'animal_id': animal_id
            },
            ConditionExpression="attribute_exists(animal_id)"
        )

        # 4. Respuesta exitosa
        return {
            'statusCode': 200,
            'body': json.dumps({'mensaje': 'Animal eliminado correctamente.'})
        }

    except Exception as e:
        print(f"Error al eliminar el animal: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Error interno del servidor.'})
        }
