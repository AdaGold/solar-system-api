STEPS TO START:
SETUP:
`git pull`
for latest changes

STEP 1: 
login to postgres
`psql -U postgres`

CREATE DATABASE for project
`CREATE DATABASE solar_system_api;`

verify in db list using
`\l`

# setup migration 
kind of iffy here tbh on what needs to be done by everyone using repo
so 
# https://learn-2.galvanize.com/cohorts/2836/blocks/1310/content_files/building-an-api/models-setup.md
here's the reference for it

do a `flask db init` for one time setup

generate migrations (dont think you need this)
`flask db migrate -m "message here"


upgrade db
`(venv) $ flask db upgrade`

check it using
`psql -U postgres`
`\c solar_system_api`
`SELECT * FROM planet;`

does it look like :
```
 id | name | description | cycle_len 
----+------+-------------+-----------
(0 rows)
```


 