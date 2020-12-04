# Spark-based Feature Store

- This project presents a feature store approach using Pyspark, within a simple, flexible and reliable structure.

- All components are containerized, such as Spark, Cassandra, Hadoop, Hive, PostgreSQL, by docker-compose.

- For the restricted, and limited development time, I do not inventing the wheel, so I'm using a framework that abstracts a good part of the Pyspark components, such as Kafka integration, DataFrames transformations, and saving it into data storages. From a pipeline structure, all Spark transformations can be organized and applied both for online and offline features. By the end, the only Spark action is to save the data into two data destinations, hive metastore for offline, and Cassandra for online features.

- The Butterfree (https://github.com/quintoandar/butterfree) is an open-source framework, developed by QuintoAndar, and serves well for prototype and when the scope is small or medium in size.


How to use it:
-----

Clone repository:

    git clone https://github.com/rafaelsandroni/spark-based-feature-store
    cd Spark-based-feature-store

Docker-compose:

    docker-compose up
    
    - spark-app will run the pipeline

Execution:

- When you run docker-compose, the spark-app container will run the pipeline and show, at the end, a query consuming data from online and offline features.
- But you can open the notebooks (in ./notebooks), and do it yourself.

Project structure (into spark-based-feature-store folder):

    notebooks 
    src
        conf
        connectors
        pipeline.py
        extract.py
        tranform.py
        load.py


Ports:    
    TCP 4041, Spark UI
