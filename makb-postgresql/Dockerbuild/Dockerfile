# Create Docker image for PostgreSQL to host MAKB
FROM postgres:9.6.16
# Install PostGIS extensions
RUN apt-get update && apt-get install -y postgresql-9.6-postgis-3
# Set default postgres password
ENV POSTGRES_PASSWORD postgres
# Seed initial database
COPY create-db.sql /docker-entrypoint-initdb.d/
RUN chmod a+r /docker-entrypoint-initdb.d/*

# PostgreSQL listens on port 5432
EXPOSE 5432