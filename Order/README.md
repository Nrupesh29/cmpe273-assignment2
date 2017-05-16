# Order API's

## Create Order
| Request | Endpoint          | Description                                |
|---------|-------------------|--------------------------------------------|
| POST    | `/order`           | Add a new Order                             |

#### Request Body:
```json
{   
    "menu_id": "xxxxxxxx",
    "order_id": "uuid_generated_by_client",
    "customer_name": "John Smith",
    "customer_email": "foobar@gmail.com"
}
```

## Update Order
| Request | Endpoint          |  Description                                |
|---------|-------------------|--------------------------------------------|
| DELETE  | `/order/{order-id}` |   Update order with specified **`order-id`**   |

#### Request Body:
```json
{   
    "input": "1"
}
```

## Get Order
| Request | Endpoint          | Description                                |
|---------|-------------------|--------------------------------------------|
| GET    | `/order/{order-id}`           | List order with specified **`order-id`**                            |
