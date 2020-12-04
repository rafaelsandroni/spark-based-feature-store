# Spark-based Online and Offline Feature Store
- A feature store approach using Pyspark, a simple, flexible and reliable structure.
- All componentes are containerized, Spark, Cassandra, Hadoop, Hive, PostgreSQL, by docker-compose.
- For the limited development time, I choose not to invent the wheel again, and use a framework that abstracts a good part of the Pyspark components, such as integration with Kafka, DataFrames transformations, and data storage. The butterfree (https://github.com/quintoandar/butterfree) is an open source and Brazilian framework, developed by QuintoAndar, and serves well when the scope is small or medium in size.


How to use
-----

Clone repository:

    git clone https://github.com/rafaelsandroni/spark-based-feature-store
    cd Spark-based-feature-store

Run docker-compose:

    docker-compose up -d
    
Open python project folder and run pipeline:

    cd spark-based-feature-store
    python src/pipeline.py

Consuming features:

    Open example notebooks in spark-based-feature-store/notebooks