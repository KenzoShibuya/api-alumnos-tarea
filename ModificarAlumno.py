import boto3

def lambda_handler(event, context):
    # Entrada (JSON)
    tenant_id = event['tenant_id']
    alumno_id = event['alumno_id']
    nuevo_datos = event['alumno_datos']
    
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')
    
    response = table.update_item(
        Key={
            'tenant_id': tenant_id,
            'alumno_id': alumno_id
        },
        UpdateExpression="SET alumno_datos = :val",
        ExpressionAttributeValues={
            ':val': nuevo_datos
        },
        ReturnValues="UPDATED_NEW"
    )
    
    # Salida (JSON)
    return {
        'statusCode': 200,
        'message': 'Registro modificado exitosamente',
        'actualizacion': response.get('Attributes')
    }