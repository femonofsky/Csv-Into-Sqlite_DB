#!/usr/bin/env python

import os
import sqlite3
import unittest
import tempfile
from io import BytesIO, StringIO


from csv_to_sqlite import process_csv_file
from query_library import get_column_names


DEFAULT_TABLE_NAME = 'data'
# TEMP_DB_PATH = os.path.join(tempfile.gettempdir(), 'test.db')
# TEMP_FILE_PATH = os.path.join(tempfile.gettempdir(), 'test_csv.csv')

SQLITE_DB_PATH = './test.db'
TEMP_FILE_PATH = './test_csv.csv'


class TESTCASE(unittest.TestCase):
    def setUp(self):
       pass

    def test_csv_file(self):
        """
         Test Function
        :return:
        """
        data = '''heading_1,heading_2,heading_3
                                       abc,1,1.0
                                       xyz,2,2.0
                                       efg,3,3.0'''
        with open(TEMP_FILE_PATH, 'w') as file:
            file.write(data)

        number_of_records = process_csv_file(TEMP_FILE_PATH, SQLITE_DB_PATH)

        self.assertEqual(number_of_records, 3)

    def test_missing_col(self):
        """
            Test for When Col is Missing
        :return:
        """
        data = '''heading_1,heading_2,heading_3
                                       abc,1.0
                                       xyz,2,2.0
                                       efg,3'''
        with open(TEMP_FILE_PATH, 'w') as file:
            file.write(data)

        number_of_records = process_csv_file(TEMP_FILE_PATH, SQLITE_DB_PATH)

        self.assertEqual(number_of_records, 1)

    def test_header(self):
        """
            Test If csv header is the same as the table column names
        :return:
        """
        data = '''wew,la,me
                                       1,2,3
                                       3,4,5
                                       6,7,8'''
        with open(TEMP_FILE_PATH, 'w') as file:
            file.write(data)

        process_csv_file(TEMP_FILE_PATH, SQLITE_DB_PATH)

        connect = sqlite3.connect(SQLITE_DB_PATH)

        cursor = connect.cursor()

        columns_ = get_column_names(cursor, DEFAULT_TABLE_NAME)

        columns = [column_[1] for column_ in columns_]

        default_header = ['wew', 'la', 'me']

        self.assertEqual(len(default_header), len(columns))

        self.assertEqual(default_header, columns)


if __name__ == '__main__':
    unittest.main()