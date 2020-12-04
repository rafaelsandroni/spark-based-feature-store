""" Feature Transformations """
from pyspark.sql import functions as F
from pyspark.sql import Window as W

def count_items(df, parent_feature, column):
    
    name = parent_feature.get_output_columns()[0]
    
    #df = df.withColumn(name, F.lit(10))
    df = df.withColumn(name, F.size(F.split(F.col(column), r"name")) - 1)
    
    return df

def avg_last_1_month(df, parent_feature, column):

    days = lambda i: i * 86400 # convert days to seconds
    
    name = parent_feature.get_output_columns()[0]
    
    windowSpec = W.partitionBy("customer_id").orderBy(F.col("order_created_at").cast('long')).rangeBetween(-days(30), 0)
    
    df = df.withColumn(name, F.avg(column).over(windowSpec))

    return df

def divide(df, fs, column1, column2):
    name = fs.get_output_columns()[0]
    df = df.withColumn(name, F.col(column1) / F.col(column2))
    return df
