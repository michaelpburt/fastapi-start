FROM python:3.8-slim-buster

RUN apt-get update && \
  apt-get install -y g++

COPY doodlebug /app/doodlebug
COPY requirements.txt /requirements.txt

ENV PYTHONPATH=/app

RUN cd /app && \
  pip install -r /requirements.txt

EXPOSE 8000

CMD ["uvicorn", "doodlebug.main:app", "--host", "0.0.0.0", "--port", "8000"]
