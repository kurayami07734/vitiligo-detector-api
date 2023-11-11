FROM python:3.11-slim
ENV PYTHONBUFFERED True

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


ENV APP_HOME /root
WORKDIR $APP_HOME
COPY /app $APP_HOME/app
COPY /tars $APP_HOME/tars
RUN cat tars/* | tar xzvf -

EXPOSE 8080
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
