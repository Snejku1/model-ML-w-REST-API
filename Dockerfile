# Użyj oficjalnego obrazu Pythona jako bazowego
FROM python:3.9-slim

# Ustawienie katalogu roboczego
WORKDIR /app

# Skopiowanie zawartości bieżącego katalogu do obrazu
COPY . /app

# Instalacja potrzebnych pakietów
RUN pip install --no-cache-dir -r requirements.txt

# Udostępnienie portu 5000
EXPOSE 5000

# Zdefiniowanie zmiennej środowiskowej
ENV NAME PerceptronApp

# Uruchomienie pliku app.py przy starcie kontenera
CMD ["python", "app.py"]
