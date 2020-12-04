
from pyspark.sql.types import StringType, IntegerType, StructType, StructField, DoubleType, BinaryType, TimestampType, DateType
import os 
kafka_connection_string: str = "a49784be7f36511e9a6b60a341003dc2-1378330561.us-east-1.elb.amazonaws.com:9092"


kafka_orders_schema = StructType([
                        StructField('cpf', IntegerType(), True),
                        StructField('customer_id', StringType(), True),
                        StructField('merchant_id', StringType(), True),
                        StructField('items', StringType(), True),
                        StructField('order_total_amount', DoubleType(), True),
                        StructField('delivery_address_latitude', DoubleType(), True),
                        StructField('delivery_address_longitude', DoubleType(), True),
                        StructField('order_scheduled', IntegerType(), True),
                        StructField('order_created_at', TimestampType(), True)
                ])

kafka_restaurants_schema = StructType([
    
                        StructField('id', StringType(), True),
                        StructField('average_ticket', DoubleType(), True),
                        StructField('takeout_time', IntegerType(), True),
                        StructField('delivery_time', IntegerType(), True),
                ])

offsets = {'de-order-events': 3682000,'de-restaurant-events': 7200}