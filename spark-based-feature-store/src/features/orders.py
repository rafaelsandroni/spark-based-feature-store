""" Features """

from features.transformations import count_items, avg_last_1_month, divide
from butterfree.transform.features import Feature
from butterfree.constants import DataType
from butterfree.transform.transformations import CustomTransform

def count_items_in_order():
    return Feature(
        name="items_qtd",
        description="count number of items in order",
        dtype=DataType.INTEGER,
        transformation=CustomTransform(
           transformer=count_items, column="items"
        )
    )

def avg_order_total_amount_from_last_1_month():
    return Feature(
        name="avg_order_amount_from_last_1_month_val",
        description="average order amount from last 1 month",
        dtype=DataType.DOUBLE,
        transformation=CustomTransform(
           transformer=avg_last_1_month, column="order_total_amount"
        )
    )

def order_total_amount():
    return Feature(
        name="order_total_amount",
        description="name_employer",
        dtype=DataType.STRING,
    )

def ratio_order_amount_and_items():
    return Feature(
        name="ratio_order_amount_by_items_val",
        description="ratio order amount by items count",
        dtype=DataType.DOUBLE,
        transformation=CustomTransform(
           transformer=divide, column1="order_total_amount", column2="items_qtd"
        )
    )

def ratio_order_amount_and_average_ticket():
    return Feature(
        name="ratio_order_amount_by_average_ticket_val",
        description="ratio order amount by restaurant average ticket",
        dtype=DataType.DOUBLE,
        transformation=CustomTransform(
           transformer=divide, column1="order_total_amount", column2="average_ticket"
        )
    )