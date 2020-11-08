#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 00:52:05 2020
"""


import psycopg2
from config import config
#from sql_queries import create_table_queries, drop_table_queries


def connect():
    """
    Establish database connection and return's the connection and cursor references.
    :return: return's (cur, conn) a cursor and
    """
    conn = None

    try:
        # Read connection parameters
        params = config()

        # connect to a PostgreSQL server
        print("Connecting to the PostgreSQL database ...")
        conn = psycopg2.connect(**params)

        # Create a cursor
        conn.set_session(autocommit=True)
        cur = conn.cursor()
        print("Connection Established!!")

    except (Exception, psycopg2.DataError) as error:
        print(error)

    finally:

        if conn is not None:

            # Create ssparkify database with UTF-8 encoding
            cur.execute("DROP DATABASE IF EXISTS sparkifydb")
            cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

            # Close connection to default database
            conn.close()

            # connect to sparkify database
            params['database'] = 'sparkifydb'
            conn = psycopg2.connect(**params)
            cur = conn.cursor()

            return conn, cur

# if __name__ == '__main__':
#     connect()
