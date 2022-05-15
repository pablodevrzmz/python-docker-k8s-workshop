# Imagen base para la aplicacion
FROM python:3.10

# Directorio donde quiero seguir mi pipeline
WORKDIR /app

# Copiar el codigo fuente a la carpeta /app
COPY ./requirements.txt /app/requirements.txt

# Instalar las dependencias
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copiar el codigo fuente a la carpeta /app
COPY . /app

# No docker-compose approach
# Agregamos las variables de ambiente
#ENV MONGO_USER='admin'
#ENV MONGO_PASS='admin'
#ENV MONGO_DB='workshop'
#ENV MONGO_SERVER='workshop-cluster.ajivk.mongodb.net'

# Exponer el puerto del subscription manager con uvicorn
EXPOSE 8005

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8005"]

#docker build . -t workshop-server   
#docker run -p 8005:8005 workshop-server