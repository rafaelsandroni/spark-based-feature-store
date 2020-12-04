from connectors.cassandra import get_config, create_table
from butterfree.load import Sink
import pyspark 
from butterfree.load.writers import (
    HistoricalFeatureStoreWriter,
    OnlineFeatureStoreWriter,
)

def loader(features_set_df: pyspark.sql.DataFrame) -> Sink:

    db_config = get_config()

    keyspace = "feature_store"
    table_name = "orders_feature_master_table_"
    primary_key = "customer_id"
    
    create_table(features_set_df, keyspace, table_name, primary_key)

    writers = [HistoricalFeatureStoreWriter(debug_mode=True), OnlineFeatureStoreWriter(db_config=db_config)]

    #writers = [HistoricalFeatureStoreWriter(debug_mode=True)]

    sink = Sink(writers=writers)
    return sink