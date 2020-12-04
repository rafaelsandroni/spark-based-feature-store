from conf import constants
from features.orders import count_items_in_order, avg_order_total_amount_from_last_1_month, ratio_order_amount_and_items, ratio_order_amount_and_average_ticket
from butterfree.transform import FeatureSet
from butterfree.transform.features import Feature, KeyFeature, TimestampFeature
from butterfree.constants import DataType

def transformer():


    # primary key
    keys = [
        KeyFeature(
            name="customer_id",
            description="Unique identificator code for customer.",
            from_column="customer_id",
            dtype=DataType.STRING,
        )
    ]

    ts_feature = TimestampFeature(from_column="order_created_at")

    # features transformations
    features = [
        #order_total_amount(),
        count_items_in_order(),
        avg_order_total_amount_from_last_1_month(),
        ratio_order_amount_and_items(),
        ratio_order_amount_and_average_ticket()
    ]

    # joining all together
    feature_set = FeatureSet(
        name="orders_feature_master_table",
        entity="orders_feature_master_table",  # entity: to which "business context" this feature set belongs
        description="Features describring events about ifood store.",
        keys=keys,
        timestamp=ts_feature,
        features=features,
    )

    return feature_set