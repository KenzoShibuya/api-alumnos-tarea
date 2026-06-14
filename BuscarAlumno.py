import boto3

def lambda_handler(event, context):
    # Entrada (JSON desde el body debido a la integración lambda)
    tenant_id = event['body']['tenant_id']
    alumno_id = event['body']['alumno_id']
    
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')
    
    response = table.get_item(
        Key={
            'tenant_id': tenant_id,
            'alumno_id': alumno_id
        }
    )
    
    # Extraer el elemento si existe en la respuesta
    item = response.get('Item', None)
    
    # Salida (JSON)
    if item:
        return {
            'statusCode': 200,
            'alumno': item
        }
    else:
        return {
            'statusCode': 404,
            'message': 'Alumno no encontrado'
        }