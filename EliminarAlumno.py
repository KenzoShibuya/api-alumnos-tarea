import boto3

def lambda_handler(event, context):
    # Entrada (JSON)
    tenant_id = event['tenant_id']
    alumno_id = event['alumno_id']
    
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')
    
    response = table.delete_item(
        Key={
            'tenant_id': tenant_id,
            'alumno_id': alumno_id
        }
    )
    
    # Salida (JSON)
    return {
        'statusCode': 200,
        'message': 'Registro eliminado exitosamente'
    }