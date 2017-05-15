import boto3
from boto3.dynamodb.conditions import Key, Attr

def lambda_handler(event, context):

    order_id = event['order_id']

    dynamodb = boto3.resource('dynamodb')
    
    table = dynamodb.Table('Orders')
    
    response = table.query(
        KeyConditionExpression=Key('orderId').eq(order_id)
    )
    
    return response['Items'][0]['payload']