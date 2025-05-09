# 1. base image
FROM python:3.11-slim

# 2. environment hygiene
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    # where Flask looks for the app instance dir
    FLASK_ENV=production

# 3. create workdir inside the image
WORKDIR /app

# 4. install Python deps first (for layer‑caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. copy the rest of the project
COPY . .

# 6. guarantee the SQLite “instance” directory exists
RUN mkdir -p /app/instance

# 7. expose Flask port
EXPOSE 5000

# 8. launch
CMD ["python", "run.py"]