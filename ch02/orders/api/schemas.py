# We define every schema as a class that inherits from pydantic’s BaseModel
# class, and we specify the type of every attribute using Python type hints

# For attibutes that can only take on a limited selection of values, we define an enumeration class

from datetime import datetime
from enum import Enum
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, Field, conlist, conint, validator, field_validator


class Size(Enum):  # Enumeration schema
    small = 'small'
    medium = 'medium'
    big = 'big'


class Status(Enum):
    created = 'created'
    progress = 'progress'
    cancelled = 'cancelled'
    dispatched = 'dispatched'
    delivered = 'delivered'


class OrderItemSchema(BaseModel):  # Every pydantic model inherits from pydantic's BaseModel
    product: str                   # Python's type hints to specify the type of attribute
    size: Size                     # Constrain the values of a property by setting its type to an enumeration
    quantity: Optional[conint(ge=1, strict=True)] = 1  # quantity’s minimum value, and we give it a default

    # @validator('quantity')
    @field_validator('quantity')
    def validate_quantity(cls, value):
        # if value < 1:
        #     raise ValueError('Quantity must be greater than 0')
        assert value is not None and value > 0, 'Quantity must be greater than 0'
        return value


class CreateOrderSchema(BaseModel):
    order: conlist(OrderItemSchema, min_length=1)  # Pydantic's conlist type to define a list with at least one element


class GetOrderSchema(CreateOrderSchema):
    id: UUID
    created: datetime
    status: Status


class GetOrdersSchema(BaseModel):
    orders: List[GetOrderSchema]


