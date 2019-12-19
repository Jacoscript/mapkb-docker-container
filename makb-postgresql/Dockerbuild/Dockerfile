# Create Docker image for PostgreSQL to host MAKB
FROM postgres:9.6.16
# Set default postgres password
ENV POSTGRES_PASSWORD postgres
#RUN su -c 'postgres'
# Seed initial database
COPY create-db.sql /docker-entrypoint-initdb.d/
RUN chmod a+r /docker-entrypoint-initdb.d/*
# PostgreSQL listens on port 5432
EXPOSE 5432