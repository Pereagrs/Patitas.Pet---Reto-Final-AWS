import json
import boto3
import time
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Animales')

def lambda_handler(event, context):
    try:
        # 1. Parsear el cuerpo recibido en formato JSON
        body = json.loads(event['body'])

        protectora_id = body.get('protectora_id')
        nombre = body.get('nombre')
        especie = body.get('especie')

        # 2. Validar campos obligatorios
        if not protectora_id or not nombre or not especie:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Faltan datos obligatorios: protectora_id, nombre o especie.'})
            }

        # 3. Generar un ID único sencillo
        animal_id = body.get('animal_id') or f"a-{int(time.time())}"

        # 4. Construir el objeto del animal
        item = {
            'protectora_id': protectora_id,
            'animal_id': animal_id,
            'nombre': nombre,
            'especie': especie,
            'edad': body.get('edad'),
            'tamaño': body.get('tamaño'),
            'estado': body.get('estado', 'disponible'),
            'foto_url': body.get('foto_url'),
            'descripcion': body.get('descripcion', ''),
            'creado_en': datetime.utcnow().isoformat()
        }

        # 5. Guardar en DynamoDB
        table.put_item(Item=item)

        # 6. Respuesta exitosa
        return {
            'statusCode': 200,
            'body': json.dumps({
                'mensaje': 'Animal creado correctamente.',
                'animal_id': animal_id
            })
        }

    except Exception as e:
        print(f"Error al crear el animal: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Error interno del servidor.'})
        }
