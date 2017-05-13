import boto3
from boto3.dynamodb.conditions import Key, Attr

def lambda_handler(event, context):

    menu_id = event['menu_id']

    dynamodb = boto3.resource('dynamodb')
    
    table = dynamodb.Table('Menus')
    
    response = table.query(
        KeyConditionExpression=Key('menuId').eq(menu_id)
    )
    
    return response['Items'][0]['payload']