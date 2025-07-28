import boto3
import os
import datetime

dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
    table_name = os.environ['Animales']  # Nombre de la tabla DynamoDB, pasado como variable de entorno
    s3_bucket = os.environ['patitas-backups-dynamo']    # Nombre del bucket S3 destino, pasado como variable de entorno
    
    # Formatear fecha actual para identificar exportación (opcional)
    export_time = datetime.datetime.utcnow().strftime('%Y-%m-%d-%H-%M-%S')
    
    try:
        response = dynamodb.export_table_to_point_in_time(
            TableArn=f'arn:aws:dynamodb:{os.environ["us-east-1"]}:{context.invoked_function_arn.split(":")[4]}:table/{table_name}',
            S3Bucket=s3_bucket,
            ExportFormat='DYNAMODB_JSON',  # O 'ION' si prefieres
            S3Prefix=f'exports/{table_name}/{export_time}'
        )
        
        export_arn = response['ExportDescription']['ExportArn']
        
        return {
            'statusCode': 200,
            'body': f'Exportación iniciada exitosamente: {export_arn}'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error iniciando exportación: {str(e)}'
        }
