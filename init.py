# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 23:07:31 2018

@author: Tuan Nguyen @ quangtuan1412@gmail.com

"""
import sqlite3 as sql

if __name__ == "__main__":
    db = sql.connect('parking.sql')
    db.execute("CREATE TABLE card(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, cardnumber CHAR NOT NULL)")
    db.commit()
    db.close()
