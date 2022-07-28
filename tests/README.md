# WALLABY database tests

The tests cover all CRUD (create, read, update and delete) operations for the Django ORM used to access the WALLABY database.

To be run in a dedicated testing environment. Do not run tests in production environment.

Make a `.env` file in this directory with the following fields

```
DJANGO_SETTINGS_MODULE = "orm.settings"
DATABASE_HOST = "localhost"
DATABASE_NAME = "wallabydb"
DATABASE_USER = <user>
DATABASE_PASS = <password>
```
