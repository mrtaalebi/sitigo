psql << EOSQL
CREATE USER sitigouser PASSWORD 'passopassopassa';
CREATE DATABASE sitigodb;
GRANT ALL PRIVILEGES ON DATABASE sitigodb to sitigouser;
EOSQL

psql sitigodb < /docker-entrypoint-initdb.d/dump
