import boto3
import json
from boto3.dynamodb.conditions import Key, Attr

def lambda_handler(event, context):

    menu_id = event['menu_id']

    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('Menus')
    
    event.update({"sequence": [
        "selection",
        "size"
    ]})

    table.put_item(
        Item={
            'menuId': menu_id,
            'payload': event
        }
    )