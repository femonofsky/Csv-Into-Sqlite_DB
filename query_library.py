

"""
    Query library
"""

import sqlite3
import csv
import sys


def get_table_names(cursor):
    """
        Get Table Number in the DB
    :param cursor:
    :return: list
    """
    cursor.execute("SELECT * FROM sqlite_master WHERE type='table'")
    return cursor.fetchall()


def get_column_names(cursor, table_name):
    """
        Get Column Names For a Table
    :param cursor:
    :param table_name: string
    :return: list
    """
    cursor.execute('PRAGMA table_info({0})'.format(table_name))
    return cursor.fetchall()


def get_rows_from_table(cursor, table_name):
    """
        Get All Rows From Table
    :param cursor:
    :param table_name: string
    :return: list
    """
    cursor.execute('SELECT * FROM {0}'.format(table_name))
    return cursor.fetchall()


def drop_table(cursor, table_name):
    """
        Drop Table if Exists
    :param cursor:
    :param table_name: string
    :return:
    """
    query = 'DROP TABLE IF EXISTS %s' % (table_name)
    return cursor.execute(query)


def create_table(cursor, table_name, columns):
    """
        Create Table
    :param cursor:
    :param table_name: string
    :param columns: list
    :return:
    """
    create_query = 'CREATE TABLE %s (%s)' % (table_name, columns)
    return cursor.execute(create_query)


def insert_into_table(cursor, table_name, data, col_length):
    """
        Insert Row into Table
    :param cursor:
    :param table_name: string
    :param data: list
    :param col_length: int
    :return:
    """
    insert_query = 'INSERT INTO %s VALUES (%s)' % (table_name,
                                                   ','.join(['?'] * col_length))
    return cursor.execute(insert_query, data)


def get_number_of_row_in_table(cursor, table_name):
    """
        Get Number of Row In The Table
    :param cursor:
    :param table_name: string
    :return: int
    """
    query = "SELECT COUNT(*) FROM {0}".format(table_name)
    cursor.execute(query)
    return cursor.fetchone()[0]


