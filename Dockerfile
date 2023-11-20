FROM python:3.12.0

# Configura el entorno
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Crea y configura el directorio de trabajo
WORKDIR /app

# Copia los archivos de requerimientos e instálalos
COPY ./requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copia el resto de la aplicación
COPY . /app/

# Comando para ejecutar la aplicación
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "Voluntariado.wsgi:application"]
