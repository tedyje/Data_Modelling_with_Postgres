#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 19:27:25 2020

@author: tewodros
"""
import os
import glob
import psycopg2
import pandas as pd
from sql_queries import * 

def process_song_file(cur, filepath):
    """
    Process songs files and insert records into the Postgres database.
    :param cur: cursor reference
    :param filepath: complete file path for the file to load
    """
    
    #open song file
    df = pd.DataFrame([pd.read_json(filepath,typ = 'series', convert_dates = False)])
    
    for value in df.values:
        num_songs, artist_id, artist_latitude, artist_longitude, artist_location, \
            artist_name, song_id, title, duration, year = value
        
        # insert artist record
        artist_data = (artist_id, artist_name, artist_location, artist_latitude, artist_longitude)
        cur.execute(artist_table_insert, artist_data)
        
        #insert song record
        song_data = (song_id, title, artist_id, year, duration)
        cur.execute(song_table_insert, song_data)
        
    print(f"Records inserted for file {filepath}")


def process_log_file(cur, filepath):
    """
    Process Even log files and insert records into the postgres database.
    :param cur: Cursor reference
    :param filepath: Complete file path for the file to load
    
    """
    # Open log files
    df = pd.read_json(filepath, lines = True)
    
    # Filter by NextSong action
    
    
def process_log_file(cur, filepath):
    """
    Process Event log files and insert records into the Postgres database.
    :param cur: cursor reference
    :param filepath: complete file path for the file to load
    """
    # open log file
    df = df = pd.read_json(filepath, lines=True)

    # filter by NextSong action
    df = df[df['page'] == "NextSong"].astype({'ts': 'datetime64[ms]'})

    # convert timestamp column to datetime
    t = pd.Series(df['ts'], index=df.index)
    
    # insert time data records
    column_labels = ["timestamp", "hour", "day", "weelofyear", "month", "year", "weekday"]
    time_data = []
    for data in t:
        time_data.append([data ,data.hour, data.day, data.weekofyear, data.month, data.year, data.day_name()])
        time_df = pd.DataFrame.from_records(data = time_data, columns = column_labels)

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = df[['userId','firstName','lastName','gender','level']]

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data = ( row.ts, row.userId, row.level, songid, artistid, row.sessionId, row.location, row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)






