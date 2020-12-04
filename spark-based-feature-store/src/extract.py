from connectors.kafka import kafka_connector
from conf import constants
from butterfree.extract.source import Source 

def extractor() -> Source:

    orders_reader = kafka_connector(
        event_id="order_events",
        topic="de-order-events",
        schema=constants.kafka_orders_schema    
    )

    restaurants_reader = kafka_connector(
        event_id="restaurants_events",
        topic="de-restaurant-events",
        schema=constants.kafka_restaurants_schema,
        
    )

    readers = [
        orders_reader,
        restaurants_reader        
    ]

    query = """
    select
        *
    from
        order_events
        join restaurants_events
            on order_events.merchant_id = restaurants_events.id
    """

    source = Source(readers=readers, query=query)
    
    return source