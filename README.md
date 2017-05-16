# PIZZA ORDERING SYSTEM

<!--
BASE_URL : https://i45r9egknb.execute-api.us-west-1.amazonaws.com/deploy
-->

### Menu API Calls

| Request | Endpoint          | Request Body       | Description                                |
|---------|-------------------|------------------- | -------------------------------------------|
| POST    | `/menu`           | [Sample Body](https://github.com/Nrupesh29/cmpe273-assignment2/blob/master/Menu/README.md#request-body)                   | Add a new Menu                             |
| DELETE  | `/menu/{menu-id}` |                    | Delete menu with specified **`menu-id`**   |
| GET     | `/menu/{menu-id}` |                    | List menu with specified **`menu-id`**     |
| PUT     | `/menu/{menu-id}` |                    | Update menu with specified **`menu-id`**   |


### Order API Calls

| Request | Endpoint            | Request Body       | Description                                 |
|---------|---------------------|------------------- | --------------------------------------------|
| POST    | `/order`            | [Sample Body](https://github.com/Nrupesh29/cmpe273-assignment2/tree/master/Order#request-body)                   | Add a new Order                             |
| GET     | `/order/{order-id}` |                    | List order with specified **`order-id`**    |
| PUT     | `/order/{order-id}` | [Sample Body](https://github.com/Nrupesh29/cmpe273-assignment2/tree/master/Order#request-body-1)                   | Update order with specified **`order-id`**  |
