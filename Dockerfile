FROM library/postgres:12.2

RUN apt-get update && apt-get upgrade -y && apt-get install -y vim && \
    apt-get install -y postgresql-contrib && \
    apt-get install -y postgresql-12-postgis-3 && \
    apt-get install -y postgresql-12-pgsphere 

COPY src/*.sql /docker-entrypoint-initdb.d/