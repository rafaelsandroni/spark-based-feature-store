FROM jupyter/all-spark-notebook

WORKDIR /home/jovyan/work

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY notebooks notebooks
COPY src src

EXPOSE 8888
EXPOSE 4040
EXPOSE 4041

