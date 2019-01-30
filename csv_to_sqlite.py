#!/usr/bin/env python

"""Extract from csv file into Sqlite DB
Usage:
    python csv_to_sqlite.py <csv_file> <?sqlite_db> <?table_name>
    :argument  csv_file the csv file location :required
    :argument sqlite_db is the location of the sqlite DB :optional
    :argument table_name is the table :optional :default is 'data'
"""

import sys
import csv
import sqlite3
import argparse
from query_library import *
from six import string_types, text_type


def process_csv_file(file_path, sqlite_db, table_name="data"):
    """
        Process csv file into sqlite DB
    Arguments:
        :param file_path: str
            The path to the csv path
        :param sqlite_db: str
            The location of the sqlite DB where the data would be save to
        :param table_name: str
            The Table Name
    :return: int
        Return the total number of Record successfully inserted into the sqlite DB
    """
    try:
        file = open(file_path, mode='r')
    except FileNotFoundError:
        print(' No such file or directory: ', file_path)
        sys.exit()

    try:
        # Analyze the file and return a Dialect reflecting the parameters found.
        dialect = csv.Sniffer().sniff(file.readline())
    except TypeError:
        dialect = csv.Sniffer().sniff(str(file.readline()))

    # Sets the position of the reader pointer to the top of the file.
    file.seek(0)

    reader = csv.reader(file, dialect)

    # Get the Headers
    headers = [header.strip() for header in next(reader)]

    # Create a connection for sqlite
    conn_ = sqlite3.connect(sqlite_db)
    _cursor = conn_.cursor()

    # Drop table if exists
    drop_table(_cursor, table_name)

    # Create table
    create_table(_cursor, table_name, ",".join(headers))

    line = 0
    for row in reader:
        line += 1

        # Check if row count is the same with the header length

        if(len(row) != len(headers)):
            print("ERROR: Wrong number of fields on row " + str(line))
            continue

        # Insert into table
        insert_into_table(_cursor, table_name, row, len(headers))
        print(str(line) + ' records inserted')

    # Get number of records inserted
    total_records = get_number_of_row_in_table(_cursor, table_name)

    file.close()
    conn_.commit()

    _cursor.close()

    return total_records


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='''
                        Convert a CSV file to a table in a SQLite database.
                        The database is created if it does not yet exist.
                ''')
    parser.add_argument('csv_file', type=str, help='Input CSV file path')
    parser.add_argument('sqlite_db', type=str, nargs='?', help='Output SQLite file', default='./sqlite.db')
    parser.add_argument('table_name', type=str, nargs='?', help='Name of table to write to in SQLite file',
                        default='data')

    args = parser.parse_args()

    total_records = process_csv_file(args.csv_file, args.sqlite_db, args.table_name)

    print("Total records are " + str(total_records))
