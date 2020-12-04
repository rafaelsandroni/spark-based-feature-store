
from butterfree.configs.db import CassandraConfig
from cassandra.cluster import Cluster

def get_config():
    return CassandraConfig(
        username="cassandra", 
        password="cassandra",
        host="feature_store_cassandra",
        keyspace="feature_store",
        stream_checkpoint_path="./"
    )

def create_table(df, keyspace, table_name, primary_key):

    cassandra_mapping = {
            "TimestampType": "timestamp",
            "BinaryType": "boolean",
            "BooleanType": "boolean",
            "DateType": "timestamp",
            "DecimalType": "decimal",
            "DoubleType": "double",
            "FloatType": "float",
            "IntegerType": "int",
            "LongType": "bigint",
            "StringType": "text",
            "ArrayType(LongType,true)": "frozen<list<bigint>>",
            "ArrayType(StringType,true)": "frozen<list<text>>",
            "ArrayType(FloatType,true)": "frozen<list<float>>",
        }

    cluster = Cluster(['feature_store_cassandra'])
    session = cluster.connect()

    session.execute(f"CREATE KEYSPACE IF NOT EXISTS {keyspace} WITH REPLICATION = {{ 'class' : 'NetworkTopologyStrategy', 'datacenter1' : 1 }};")

    sql = ", ".join(
        [f"{feature.name} {cassandra_mapping[str(feature.dataType)]}" for feature in df.schema]
    )

    sql = sql.replace(f"{primary_key} text", f"{primary_key} text PRIMARY KEY")
    
    sql = f"CREATE TABLE IF NOT EXISTS {keyspace}.{table_name} ({sql});"
    
    sql(print)

    session.execute(sql)
    cluster.shutdown()