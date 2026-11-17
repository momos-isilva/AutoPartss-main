# Imagen base oficial ligera de Python 3.11
FROM python:3.11-slim

# Evitar archivos .pyc y habilitar salida directa en consola
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Directorio raíz del proyecto dentro del contenedor
WORKDIR /app

# Instalar dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copiar todo el código fuente (backend, frontend y archivos de configuración)
COPY . .

# Ubicar el directorio de trabajo donde se encuentra manage.py
WORKDIR /app/backend

# Exponer el puerto de Django
EXPOSE 8000

# Comando por defecto para levantar la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]