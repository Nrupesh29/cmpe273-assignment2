# Menu API's

## Create Menu
| Request | Endpoint          | Description                                |
|---------|-------------------|--------------------------------------------|
| POST    | `/menu`           | Add a new Menu                             |

#### Request Body:
```json
{
    "menu_id": "UUID-generated-by-client",
    "store_name": "Pizza Hut",
    "selection": [
        "Cheese",
        "Pepperoni"
    ],
    "size": [
        "Slide", "Small", "Medium", "Large", "X-Large"
    ],
    "price": [
        "3.50", "7.00", "10.00", "15.00", "20.00"
    ],
    "store_hours": {
        "Mon": "10am-10pm",
        "Tue": "10am-10pm",
        "Wed": "10am-10pm",
        "Thu": "10am-10pm",
        "Fri": "10am-10pm",
        "Sat": "11am-12pm",
        "Sun": "11am-12pm"
    }
}
```

## Delete Menu
| Request | Endpoint          |  Description                                |
|---------|-------------------|--------------------------------------------|
| DELETE  | `/menu/{menu-id}` |   Delete menu with specified **`menu-id`**   |


## Update Menu
| Request | Endpoint          | Description                                |
|---------|-------------------|--------------------------------------------|
| PUT    | `/menu/{menu-id}`           | Update menu with specified **`menu-id`**                             |


## Get Menu
| Request | Endpoint          | Description                                |
|---------|-------------------|--------------------------------------------|
| GET    | `/menu/{menu-id}`           | List menu with specified **`menu-id`**                            |
