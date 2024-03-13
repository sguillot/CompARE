# Description 

Short description of files in this repository:

## database/

- `database_draft.sql`: develpement database. Use `mysql -u root -p < database_draft.sql` to create the database.
- `delete_request.sql`: command to empty the content of the database (but keeps the structure).

## get_data.py:

This script collects the data from public repositories and store them in data/. 

`$ python3 get_data.py`

### For Windows users:

If you don't have `wget` and/or `gzip`, download them from the following addresses: 

- `wget`: https://eternallybored.org/misc/wget/ (choose the latest version and download the `.exe` file to avoid SSL certificate errors).
- `gzip`: https://gnuwin32.sourceforge.net/packages/gzip.htm (download the `setup`).

## gw170817.py:

This script analyses the data and produces pdf and confidence levels.

`$ python3 gw170817.py`

**Note:** Remember to install all the necessary dependencies.
