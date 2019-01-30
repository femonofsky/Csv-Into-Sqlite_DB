#  Csv Into Sqlite_DB App

Extract from csv file into Sqlite DB.

 This Script skips any row that doesn't have the same number as the header row (first row)
## Requirements
* Python 3.4+
* Works on Linux, Windows, Mac OSX, BSD

## Usage
```
./csv_to_sqlite.py {csv_file} [{sqlite_db}] [{table_name}]

```
`csv_file` is the path to the csv file and it is required.

 `sqlite_db` is the path to the sqlite DB, create `sqlite_db` if does not exist.

 `table_name` is the name of table to write to in SQLite file use `data` as default


## Running the tests
```
python -m unittest
```

#### For Help
```
./csv_to_sqlite.py -h

```
