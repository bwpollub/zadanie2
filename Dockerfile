# pierwszy etap - pobranie obrazu bazowego i instalacja zależności systemowych
FROM python:3.10-slim-buster AS base

# ustawienie informacji o autorze
ARG AUTHOR="Bartłomiej Wójtowicz"

# instalacja zależności systemowych, które będą potrzebne do uruchomienia kodu źródłowego
RUN apt-get update

# drugi etap - stworzenie warstwy z zainstalowanymi zależnościami z Python
FROM base AS dependencies

# Ustawienie katalogu w ktorym pracujemy na app
WORKDIR /app

# skopiowanie pliku requirements.txt do folderu /app w kontenerze
COPY ./requirements.txt ./

# instalacja zależności Python
RUN pip install --no-cache-dir -r requirements.txt

# trzeci etap - stworzenie warstwy z kodem źródłowym
FROM dependencies AS application

# ustawienie portu, na którym będzie działać aplikacja
ENV PORT=8080

# dodanie uzytkownika serveruser
RUN adduser --disabled-password --gecos "" serveruser

# ustawienie katalogu w ktorym pracujemy na app
WORKDIR /app

# ustawienie dodanego uzytkownika jako wlasciciela /app
RUN chown -R serveruser:serveruser /app

# uzycie uzytkownika serveruser 
USER serveruser

# skopiowanie kodu źródłowego
COPY ./app /app/src

# dodanie informacji o autorze obrazu
LABEL maintainer=$AUTHOR

# uruchomienie serwera
CMD ["python", "src/http_server.py"]
