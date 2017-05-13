import boto3
from boto3.dynamodb.conditions import Key, Attr

def lambda_handler(event, context):

    menu_id = event['menu_id']

    dynamodb = boto3.resource('dynamodb')
    
    table = dynamodb.Table('Menus')
    
    table.delete_item(
        Key={
            'menuId': menu_id
        }
    )