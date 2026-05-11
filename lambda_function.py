import json
import boto3
import uuid
import time
from boto3.dynamodb.conditions import Key
from decimal import Decimal

# --- TRADUCTOR DE DECIMALES ---
# DynamoDB devuelve números en formato Decimal que json.dumps no entiende.
# Esta función los convierte a tipos estándar de Python.
def decimal_default(obj):
    if isinstance(obj, Decimal):
        return int(obj) if obj % 1 == 0 else float(obj)
    raise TypeError

dynamodb = boto3.resource('dynamodb')
# El nombre debe ser idéntico al de tu tabla en DynamoDB
table = dynamodb.Table('tareas-privadas')

def lambda_handler(event, context):
    # Configuración de CORS para que tu web en S3 pueda comunicarse con la API
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': 'Content-Type,Authorization',
        'Access-Control-Allow-Methods': 'OPTIONS,GET,POST,DELETE'
    }

    # Manejo de la solicitud preliminar de CORS
    if event.get('httpMethod') == 'OPTIONS':
        return {'statusCode': 200, 'headers': headers, 'body': json.dumps('OK')}

    try:
        # Extraer el ID del usuario desde el token de Cognito
        authorizer = event.get('requestContext', {}).get('authorizer', {})
        user_id = authorizer.get('claims', {}).get('sub')
        
        if not user_id:
            return {'statusCode': 401, 'headers': headers, 'body': json.dumps('No autorizado')}

        method = event.get('httpMethod')
        path_params = event.get('pathParameters')

        # --- MÉTODO GET: LISTAR TAREAS DEL USUARIO ---
        if method == 'GET':
            response = table.query(
                KeyConditionExpression=Key('userId').eq(user_id)
            )
            items = response.get('Items', [])
            return {
                'statusCode': 200, 
                'headers': headers, 
                'body': json.dumps({'items': items}, default=decimal_default)
            }

        # --- MÉTODO POST: CREAR NUEVA TAREA ---
        elif method == 'POST':
            body = json.loads(event.get('body', '{}'))
            new_task = {
                'userId': user_id,           # Partition Key
                'taskId': str(uuid.uuid4()),  # Sort Key (ID único)
                'title': body.get('title', 'Nueva Tarea'),
                'type': body.get('type', 'General'),
                'completed': False,
                'createdAt': int(time.time())
            }
            table.put_item(Item=new_task)
            return {
                'statusCode': 201, 
                'headers': headers, 
                'body': json.dumps(new_task, default=decimal_default)
            }

        # --- MÉTODO DELETE: BORRAR TAREA ---
        elif method == 'DELETE':
            # El ID viene de la URL: /tasks/{id}
            if path_params and 'id' in path_params:
                t_id = path_params['id']
                table.delete_item(
                    Key={
                        'userId': user_id,
                        'taskId': t_id
                    }
                )
                return {
                    'statusCode': 200, 
                    'headers': headers, 
                    'body': json.dumps({'msg': 'Tarea eliminada correctamente'})
                }
            else:
                return {'statusCode': 400, 'headers': headers, 'body': json.dumps('ID no proporcionado')}

    except Exception as e:
        # Si algo falla, devolvemos el error para poder debuguear en la consola del navegador
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500, 
            'headers': headers, 
            'body': json.dumps({'error': 'Error interno', 'details': str(e)})
        }
