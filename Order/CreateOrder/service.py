import boto3
from time import gmtime, strftime
from boto3.dynamodb.conditions import Key, Attr

def lambda_handler(event, context):

    menu_id = event['menu_id']
    order_id = event['order_id']
    customer_name = event['customer_name']

    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('Orders')
    
    event.update({"order_status": "incomplete",
    "orders": {
        "selection": None,
        "size": None,
        "costs": None,
        "order_time": strftime("%m-%d-%Y@%H:%M:%S", gmtime())
    }})

    table.put_item(
        Item={
            'orderId': order_id,
            'payload': event
        }
    )
    
    response = dynamodb.Table('Menus').query(
        KeyConditionExpression=Key('menuId').eq(menu_id),
    )
    
    selection_options = ""
    index = 1
    for selection in response['Items'][0]['payload']['selection']:
        selection_options = selection_options + str(index) + ". " + selection + ", "
        index += 1
    
    selection_options = selection_options[:-2]
    
    return dict({"Message": "Hi " + customer_name + ", please choose one of these selection: " + selection_options})