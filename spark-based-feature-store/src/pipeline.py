from argparse import ArgumentParser

from conf import constants
from extract import extractor as E
from transform import transformer as T
from load import loader as L

import os 
os.environ['PYSPARK_SUBMIT_ARGS'] = '--master local[6] --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.0.0,com.datastax.spark:spark-cassandra-connector_2.12:3.0.0-beta pyspark-shell'
from connectors.spark import spark_connector
from butterfree.pipelines import FeatureSetPipeline

spark_client = spark_connector()

def run():
    """ 
    Build data sources, features transformations and loaders.    
    By the end, run the entirely pipeline, and write data into loaders.
    """
    

    def _print_sample_data(df):

        # print source sample
        df = source.construct(spark_client)

        #df = df.limit(40)

        #df.show()

        return df

    # extract

    # Extract from data sources
    
    source = E()
    #_print_sample_data(source)

    # Feature transformations 
    feature_set = T()
    df = _print_sample_data(feature_set)

    # Loaders are Hive metastore (offline/historical) and Cassandra (online/realtime)
    sink = L(df)

    pipeline = FeatureSetPipeline(source=source, feature_set=feature_set, sink=sink)

    # load
    print("Running pipeline...")
    pipeline.run()


def consuming():    
    """
    Query example for consuming online and offline features.
    """
    
    print("="*100)
    print("online feature store")
    cluster = Cluster(['feature_store_cassandra'])
    session = cluster.connect()
    df = session.execute("SELECT * FROM feature_store.orders_feature_master_table")
    cluster.shutdown()
    # Create data frame
    df = spark.createDataFrame(df)
    print(df.show())
    print("="*100)
    print("historical feature store")
    print(spark.table("historical_feature_store__orders_feature_master_table").show())


if __name__ == "__main__":

    parser: ArgumentParser = ArgumentParser(
        description="Run the pipeline"
    )

    run()