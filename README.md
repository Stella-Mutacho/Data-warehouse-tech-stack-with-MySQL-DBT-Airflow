# Data-warehouse-tech-stack-with-MySQL-DBT-Airflow
The aim of this Project is to create a scalable data warehouse that will host the vehicle trajectory data extracted by analysing footage taken by swarm drones and static roadside cameras. The data warehouse will by implementing ELT data engineering methods with PostgreSQL, DBT, redash and Airflow 

## Data Flow Architechture
![image](https://user-images.githubusercontent.com/53911989/180662771-b93fc050-fb76-40ab-a5b9-814d34c16bac.png)
## Data Source
The data source is the PNEUMA dataset. The data extracted from the data source is in CSV data files sorted in a chronological order, depending on the day it was captured, the region the car was driving on and the time the records were taken. In the CSV file, the data is separated by semi colons. There are 4 columns that are uniformly defining the data. The Next six columns are repeated for every time a record an image was taken by the drones. In each record, the last of the six columns is the time the record was taken.

## Key
This repository contains the code used to build an ELT data Pipeline in accordance with the Techstack flow show above.

### Prerequisites

Docker - https://docs.docker.com/engine/install/ 

## Key

1. requirements - REquirements.txt

2. docker compose file - https://github.com/Stella-Mutacho/Data-warehouse-tech-stack-with-MySQL-DBT-Airflow/blob/main/airflow-docker/docker-compose.yml

3. Airflow DAGs -https://github.com/Stella-Mutacho/Data-warehouse-tech-stack-with-MySQL-DBT-Airflow/tree/main/airflow-docker/dags

4. extract Script- https://github.com/Stella-Mutacho/Data-warehouse-tech-stack-with-MySQL-DBT-Airflow/blob/main/scripts/extract.py

5. load to DB-https://github.com/Stella-Mutacho/Data-warehouse-tech-stack-with-MySQL-DBT-Airflow/blob/main/airflow-docker/dags/traffic_csv_to_db.py


Prerequisites

Make sure you have docker installed on local machine.

    Docker
    DockerCompose

Installation

    1. Clone the repo

    git clone https://github.com/Stella-Mutacho/Data-warehouse-tech-stack-with-MySQL-DBT-Airflow 

    2. Datawarehouse

    cd sensor_data

    Run

     3. docker-compose up

      To access and Modify the default configrations for each tool use the .env files.

## MYSQL:

    Navigate to `http://localhost:8080/` on the browser
    use `mysqldb` server
    use `airflow` database
    use `airflow` for username
    use `airflow` for password

## Postgress:

    Navigate to `http://localhost:8080/` on the browser
    use `postgres-dbt` server
    use `airflow` database
    use `airflow` for username
    use `airflow` for password

## Airflow

Airflow is used for scheduling and automation.

Navigate to `http://localhost:8080/` on the browser
use `airflow` for username
use `airflow` for password

DBT:

DBT performs the T in the ELT process, transforming the data in the warehouses.

    Airflow is used for automation of running and testing dbt models
    navigate to https://sensordataelt.herokuapp.com/index.html to access dbt docs

## Redash

open terminal and execute `docker-compose run — rm server create_db`
using adminer create a user and grant read access
Navigate to `http://localhost:5000/` on the browser

## Superset

    navigate to localhost:8088 to access Airflow

## Contribution

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

    Fork the Project
    Create your Branch (git checkout -b feature/NewFeature)
    Commit your Changes (git commit -m 'Add some NewFeature')
    Push to the Branch (git push origin feature/NewFeature)
    Open a Pull Request



