FROM python:3.10.4-alpine3.15

ENV PYTHONUNBUFFERED=1

# Crea y configura el directorio de trabajo
WORKDIR /app

# Copia los archivos de requerimientos e instálalos

RUN apk update \
    && apk add --no-cache gcc musl-dev postgresql-dev python3-dev libffi-dev \
    && pip install --upgrade pip

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

# Copia el resto de la aplicación
COPY ./ ./

# Comando para ejecutar la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]