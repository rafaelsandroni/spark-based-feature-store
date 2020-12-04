""" kafka connectors """
from conf import constants
from butterfree.extract.readers import KafkaReader

def kafka_connector(event_id: str, topic: str, schema: any) -> KafkaReader:
    return KafkaReader(
        id=event_id,
        topic=topic,
        value_schema=schema,
        connection_string=constants.kafka_connection_string,
        topic_options={"startingOffsets": f""" {{"{topic}": {{ "0":{constants.offsets[topic]} }}}} """},
        stream=False
    )