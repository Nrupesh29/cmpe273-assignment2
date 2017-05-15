import boto3
from time import gmtime, strftime
from boto3.dynamodb.conditions import Key, Attr

def lambda_handler(event, context):

    order_id = event['order_id']
    input_id = event['input']

    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('Orders')
    
    response = table.query(
        KeyConditionExpression=Key('orderId').eq(order_id)
    )
    
    menuResponse = dynamodb.Table('Menus').query(
        KeyConditionExpression=Key('menuId').eq(response['Items'][0]['payload']['menu_id'])
    )
    
    size_options = ""
    index = 1
    for size in menuResponse['Items'][0]['payload']['size']:
        size_options = size_options + str(index) + ". " + size + ", "
        index += 1
    
    size_options = size_options[:-2]
    
    if(response['Items'][0]["payload"]["orders"]['selection'] == None):
        table.update_item(
            Key={
                'orderId': order_id
            },
            UpdateExpression="set payload.orders.selection = :selection",
            ExpressionAttributeValues={
                ':selection': menuResponse['Items'][0]['payload']['selection'][int(input_id)-1]
            }
        )
        
        return dict({"Message": "Which size do you want? " + size_options})
        
    elif(response['Items'][0]["payload"]["orders"]['size'] == None):
        table.update_item(
            Key={
                'orderId': order_id
            },
            UpdateExpression="set payload.orders.size = :size, payload.orders.costs = :costs, payload.order_status = :status",
            ExpressionAttributeValues={
                ':status': 'processing',
                ':size': menuResponse['Items'][0]['payload']['size'][int(input_id)-1],
                ':costs': menuResponse['Items'][0]['payload']['price'][int(input_id)-1]
            }
        )
        
    return dict({"Message" : "Your order costs $" + menuResponse['Items'][0]['payload']['price'][int(input_id)-1] + ". We will email you when the order is ready. Thank you!"})