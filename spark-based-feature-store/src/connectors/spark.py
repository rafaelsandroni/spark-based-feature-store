from pyspark import SparkContext, SparkConf
from pyspark.sql import session, SparkSession
from pyspark.sql import HiveContext
from butterfree.clients import SparkClient

def spark_connector(app_name: str = "feature store") -> SparkClient:
    

    hive_metastore = "thrift://hive-metastore:9083"

    spark = (
        SparkSession
        .builder
        .appName("Feature Store")
        .config("spark.sql.warehouse.dir", hive_metastore)
        .config("spark.hive.metastore.uris", hive_metastore)
        .config("spark.executor.memory", "8g")
        .config("spark.executor.cores", "2")
        .config("spark.sql.shuffle.partitions", 10)
        .enableHiveSupport()
        .getOrCreate()
    )

    sc=spark.sparkContext

    spark_client = SparkClient()
    hive_context = HiveContext(sc)

    return spark_client