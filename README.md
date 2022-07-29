<h1 align="center">WALLABY Database</h1>

<!-- TODO(austin): build an official image for the WALLABY database -->

## src

The repository contains all of the `.sql` scripts (in the [`src/`](src/) folder) necessary for initialising a PostgreSQL database with the schema used for [WALLABY](https://wallaby-survey.org/) post-processing. The tables can be separated into three different groups:

* Source finding
* Kinematics
* Multi-wavelength.

Each group captures the tables required for contributions by the AusSRC, CIRADA and SpainSRC, respectively, to the production of WALLABY catalogue data. 

### Initialisation

The first script [`01-users.sql`](src/01-users.sql) is used to create the database and create the users that will be able to access the user. It will create:

* admin user (full access)
* wallaby user (read-only access)
* vo user

You will need to create a file called `psql.env` which contains the environment variable `POSTGRES_PASSWORD`.

### Source finding

The [`02-source-finding.sql`](src/02-source-finding.sql) and [`05-privileges.sql`](src/05-privileges.sql) scripts are used to create the tables required for source finding and access control. The tables are summarised below

| Name | Description |
|---|---|
| `run` | Name of the run (source finding application applied to a specific WALLABY data cube) |
| `instance` | Instance of the run (source finding application is parallelised and will split the entire WALLABY data cube into sub-cubes). |
| `detection` | Source finding application automatically identified detection. |
| `product` | Data products associated with a given detection (e.g. moment maps) |
| `source` | WALLABY admin determined source with a formal source name. |
| `source_detection` | Many-to-one table for mapping a source to detections. |
| `comment` | Comments applied to the detections table during manual inspection. |
| `tag` | Tag name and description. |
| `tag_detection` | Mapping from tags to the detections, added during manual inspection. |
| `tag_source_detection` | Mapping from tags to the `source_detection` table for specifying release data. |

### Kinematics

The [`03-kinematics.sql`](src/03-kinematics.sql) script is used to create the tables required for source finding and access control. The tables are summarised below: 

..

### Multi-wavelength

The [`04-multi-wavelength.sql`](src/04-multi-wavelength.sql) script is used to create the tables required for source finding and access control. The tables are summarised below: 

...

### Provenance

Provenance metadata allows for the results of the execution of the AusSRC WALLABY post-processing pipeline to be reproduced. This table, called `run_metadata`, links the Run with the metadata. The metadata that we include are:

* repository (location of pipeline code)
* branch (`github` branch to specify the component(s) of the pipeline that was executed)
* version (`github` version or nextflow revision of the pipeline that was executed)
* configuration (content of the `nextflow.config` file for the pipeline run)
* parameters (content of the `params.yaml` for the pipeline run)
* datetime (when the pipeline was executed)

## Deployment

**NOTE** You will need to update passwords in the [`create.sql`](src/create.sql) file for any sort of security. Currently there are default passwords which are not appropriate for a production environment. You need to change them for either of the following deployment approaches.

### Docker

The easiest method for deploying the WALLABY database is with the docker. We have provided a [`Dockerfile`](Dockerfile) that creates an PostgreSQL image with the scripts in the `src` subdirectory. To get this up and running:

```
docker-compose up --build
```

You will need to define a `psql.env` file to set environment variables for the default `postgres` user in order to deploy the container. An example one is:

```
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
```

### Manual

You can also install the schema on an existing PostgreSQL instance. You will also need to install dependencies `postgis` and `pg_sphere`. For Ubuntu and PostgreSQL 12, this can be done with the following command:

```
sudo apt install postgresql postgresql-contrib postgis sudo apt-get install postgresql-12-pgsphere
```

Once you have the dependencies you will need to initialise the database with the SQL scripts in the [`src/`](src/) subdirectory. To do this you can run the line below for each of the scripts in that directory. This is also how you can update an existing instance of the WALLABY database when there have been changes to the repository.

```
psql -h localhost -U admin -d wallabydb -f src/01-users.sql
```

## orm

We also provide an object relational mapper with SQLAlchemy that will be compatible with the database. 

### Tests

We have written some unit tests to ensure that the SQLAlchemy ORM works with the database schema. You can run them from the `orm/` directory with the following commands

```
python -m unittest tests/tests_wallaby_run.py
python -m unittest tests/tests_wallaby_instance.py
```

## Operations

The file [`src/06-operations.sql`](src/06-operations.sql) contains WALLABY tables used for managing the operations of the survey. Below are the tables and their descriptions:

| Table | Description |
| --- | --- |
| `observation` |  tracking observations and their quality ([WALLABY footprint check](https://github.com/AusSRC/WALLABY_footprint_check)) in CASDA |
| `tile` | pre-defined WALLABY tiles in the sky |
| `postprocessing` | tracking any post-processing jobs ([WALLABY pipeline](https://github.com/AusSRC/WALLABY_pipeline)) run on the tiles | 
| `mosaic` | many to many mapping from tiles to a postprocessing job |
| `prerequisite` | TBA |
| `prerequisite_identifier` | TBA |

### Important fields

#### quality

The quality field refers to whether or not the footprint has passed the manual quality control step. This step involves running the [WALLABY footprint check](https://github.com/AusSRC/WALLABY_footprint_check) pipeline on the data once it becomes available through CASDA. These are the allows values for `quality`:

| `quality` | Description |
| --- | --- |
| `NULL` | no quality check pipeline has been executed on this data |
| `PENDING` | quality check pipeline has been triggered for this footprint and is awaiting input from WALLABY  |science team
| `PASSED` | passed quality check and can be used for tiles |
| `FAILED` | failed quality check and should not be used for creating tiles  |

#### status

The status field refers to the status of the pipeline executed on the data. This can either be the quality check pipeline that we discuss in the subsection above, or the [WALLABY post-processing pipeline](https://github.com/AusSRC/WALLABY_pipeline). The allowed values are in the table below.

| `status` | Description |
| --- | --- |
| `NULL` | Pipeline has not been executed for this data |
| `QUEUED` | Slurm job for the pipeline has been submitted and is waiting to run |
| `RUNNING` | Pipeline is currently running |
| `COMPLETED` | Pipeline has run to completion |
| `FAILED` | Pipeline failed before running to completion |
