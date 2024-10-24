# Usa una imagen base de Python
FROM python:3.11-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo de la aplicación
COPY app.py .

# Instala Flask y deep-translator
RUN pip install --no-cache-dir Flask deep-translator

# Expone el puerto en el que la aplicación se ejecutará
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
