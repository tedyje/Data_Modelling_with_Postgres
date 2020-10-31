#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 02:33:51 2020

@author: tewodros
"""

from configparser import ConfigParser

def config(filename = 'database.ini', section = 'postgresql'):
    
    # Create a parser
    
    parser = ConfigParser()
    
    # read config file
    
    parser.read(filename)
    
    # get section, default to postgresql
    
    db = {}
    
    if parser.has_section(section):
        params = parser.items(section)
        
        for param in params:
            db[param[0]] = param[1]
    
    
