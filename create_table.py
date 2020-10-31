#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 00:52:05 2020

@author: tewodros
"""


import psycopg2
from config import config
from sql_queries import create_table_queries, drop_table_queries


def connect():
    """
    Establish database connection and return's the 
    connection and cursor references.
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
        
        # Execute statement
        print("PostgreSQL database version: ")
        cur.execute("SELECT version()")
        
        # Dispalcy the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
        
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
        
def drop_tables(cur, conn):
    """
    Run's all the drop table queries defined in sql_queries.py
    :param cur: cursor to the database
    :param conn: database connection reference
    
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()
        
def create_tables(cur, conn):
    """
    Run's all the create table queries defined in sql_queries.py
    :param cur: cursor to the database
    :param conn: database connection reference
    
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()
        

def main():
    """
    Driver main function
    """
    conn, cur = connect()
    
    drop_tables(cur, conn)
    print("\nTable dropped successfully!!")
    
    create_tables(cur, conn)
    print("Table created successfully!!")
    
    conn.close()

if __name__ == "__main__":
    main()

    