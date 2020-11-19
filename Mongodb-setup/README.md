# Initialize a Database

* `docker pull bitnami/mongodb:latest`

mongodb container need permission for r+w for mongodb_data file:
* `sudo chown -R 1001 /tmp/mongodb_data`