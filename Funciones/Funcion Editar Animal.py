import json
import boto3
from datetime import datetime

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

        # 3. Crear expresión de actualización dinámica
        update_expression = "SET actualizado_en = :actualizado_en"
        expression_values = {':actualizado_en': datetime.utcnow().isoformat()}
        expression_names = {}

        campos_actualizables = ['nombre', 'especie', 'edad', 'tamaño', 'estado', 'foto_url', 'descripcion']
        for campo in campos_actualizables:
            if campo in body:
                update_expression += f", #{campo} = :{campo}"
                expression_values[f":{campo}"] = body[campo]
                expression_names[f"#{campo}"] = campo

        if len(expression_values) == 1:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'No se proporcionaron campos para actualizar.'})
            }

        # 4. Ejecutar la actualización en DynamoDB
        table.update_item(
            Key={
                'protectora_id': protectora_id,
                'animal_id': animal_id
            },
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_values,
            ExpressionAttributeNames=expression_names,
            ConditionExpression="attribute_exists(animal_id)"
        )

        # 5. Respuesta exitosa
        return {
            'statusCode': 200,
            'body': json.dumps({'mensaje': 'Animal actualizado correctamente.'})
        }

    except Exception as e:
        print(f"Error al actualizar el animal: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Error interno del servidor.'})
        }
