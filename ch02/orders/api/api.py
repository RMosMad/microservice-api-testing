from datetime import datetime
from uuid import UUID  # universal unique identifier

from starlette.responses import Response
from starlette import status

from orders.app import app
from orders.api.schemas import GetOrderSchema, CreateOrderSchema, GetOrdersSchema


order = {  # This is a dictionary that represents an order.
    'id': 'ff0f1355-e821-4178-9567-550dec27a373',
    'status': 'delivered',
    'created': datetime.utcnow(),
    'order': [
        {
            'product': 'latte',
            'size': 'medium',
            'quantity': 1
        }
    ]
}


# This is a decorator that tells FastAPI to call the get_orders function when a GET request is made to /orders.
@app.get('/orders', response_model=GetOrdersSchema)
def get_orders():  # GET endpoint for the /orders route.
    return {'orders': [order]}
    # This returns a dictionary with a key of orders and a value of a list containing the order dictionary.


@app.post(
    '/orders',
    status_code=status.HTTP_201_CREATED,
    response_model=GetOrderSchema
)
def create_order(order_details: CreateOrderSchema):
    return order


@app.get('/orders/{order_id}', response_model=GetOrderSchema)
def get_order(order_id: UUID):
    """
        This function is a GET endpoint for the /orders/{order_id} route.
        It takes an order_id as an argument and returns the order dictionary.
        :param order_id: Order id. Type hinting is used to specify the type of the order_id argument: UUID.
        :return: Order dictionary
    """
    return order


@app.put('/orders/{order_id}', response_model=GetOrderSchema)
def update_order(order_id: UUID, order_details: CreateOrderSchema):
    return order


@app.delete('/orders/{order_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_order(order_id: UUID):
    """
    This function is a DELETE endpoint for the /orders/{order_id} route.
    It takes an order_id as an argument and returns a Response object with a status code of 204.
    :param order_id: Order id
    :param status_code: Status code HTTPStatus.NO_CONTENT.value to return an empty response with a status code of 204.
    :return: Response object with a status code of 204.
    """

    return Response(status_code=status.HTTP_204_NO_CONTENT.value)


@app.post('/orders/{order_id}/cancel', response_model=GetOrderSchema)
def cancel_order(order_id: UUID):
    return order


@app.post('/orders/{order_id}/pay', response_model=GetOrderSchema)
def pay_order(order_id: UUID):
    return order




