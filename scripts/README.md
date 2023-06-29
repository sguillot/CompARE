# Description 

Short description of files in this repository:

## database/

- `database_draft.sql`: develpement database. Use `mysql -u root -p < database_draft.sql` to create the database.
- `delete_request.sql`: command to empty the content of the database (but keeps the structure).

## get_data.py:

This script collects the data from public repositories and store them in data/. 

`$ python3 get_data.py`


## gw170817.py:

This script analyses the data and produces pdf and confidence levels.

`$ python3 gw170817.py`
