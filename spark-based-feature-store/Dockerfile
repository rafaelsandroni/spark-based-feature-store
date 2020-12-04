FROM jupyter/all-spark-notebook

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8888
EXPOSE 4040
EXPOSE 4041

CMD ["python", "src/pipeline.py"]
