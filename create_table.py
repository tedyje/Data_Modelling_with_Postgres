#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 00:52:05 2020

@author: tewodros
"""


# import psycopg2
# from config import config
# from sql_queries import create_table_queries, drop_table_queries
# from connect import connect
from sql_queries import *


def drop_tables(cur, conn):
    """
    Run's all the drop table queries defined in sql_queries.py
    :param cur: cursor to the database
    :param conn: database connection reference

    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()

    # print("\nTable dropped successfully!!")

def create_tables(cur, conn):
    """
    Run's all the create table queries defined in sql_queries.py
    :param cur: cursor to the database
    :param conn: database connection reference

    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()
