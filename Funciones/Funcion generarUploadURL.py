import json
import boto3
import uuid
import os

s3 = boto3.client('s3')
BUCKET_NAME = os.environ.get('BUCKET_NAME')  # Usa una variable de entorno para mayor flexibilidad

def lambda_handler(event, context):
    try:
        # Parsear el cuerpo
        body = json.loads(event['body'])
        content_type = body.get('content_type', 'image/jpeg')  # image/png, etc.

        # Validar tipo de archivo si se desea
        if not content_type.startswith('image/'):
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Tipo de archivo no permitido. Debe ser una imagen.'})
            }

        # Generar nombre único
        file_extension = content_type.split('/')[-1]
        file_name = f"animales/{uuid.uuid4()}.{file_extension}"

        # Generar URL prefirmada
        url = s3.generate_presigned_url(
            ClientMethod='put_object',
            Params={
                'Bucket': BUCKET_NAME,
                'Key': file_name,
                'ContentType': content_type
            },
            ExpiresIn=3600  # 1 hora
        )

        # Devolver URL
        return {
            'statusCode': 200,
            'body': json.dumps({
                'upload_url': url,
                'file_url': f"https://{BUCKET_NAME}.s3.amazonaws.com/{file_name}"
            })
        }

    except Exception as e:
        print(f"Error al generar la URL de subida: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Error interno del servidor.'})
        }
