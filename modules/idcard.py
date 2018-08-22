# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 13:40:47 2018

@author: Tuan Nguyen @ quangtuan1412@gmail.com
"""
import sys
import time
import serial
import MySQLdb as mysql

# import serial.tools.list_ports_windows as port_list
# ports = list(port_list.comports())

class Card:
    """
    1. Regist an ID card to system, add card number to database
    2. read ID card number, check if it is database or not 
    3. Methods: card_read(), card_add(), card_del(), card_check()
    """
    
    
    def __int__(self, cardnumber):
        self.cardnumber = cardnumber

    def card_read(self, port, baudrate):
        '''
        Read cardNumber form serial COM port (connected to Card Reader)
        return cardNumber
        '''  
        ser = serial.Serial()
        ser.close()
        ser.port = port
        ser.baudrate = baudrate
        ser.open()

        ser.flushInput() # Clear all input buffer
        time.sleep(1)
        bytesToRead = ser.inWaiting()
        data_raw = (ser.read(bytesToRead))
        if len(data_raw) > 9: 
            print(data_raw)
            cardnumber = data_raw[1:9]
            print(cardnumber)
            return cardnumber
        else:
            return None
    
    def card_check(self, cardnumber):
        '''
        check the card has cardNumber to see if it is already in database
        return True if existed, False if not
        '''
        self.cardnumber = cardnumber
        
        db = mysql.connect(host = 'localhost', user = 'root', passwd ='HongMinh1960', db = 'parking',
	charset = 'utf8')
        cursor = db.cursor()
        
        query = "SELECT * FROM card WHERE cardnumber = {}".format(self.cardnumber)
        try:
            if cursor.execute(query):
                db.commit()
                db.close()
                return True
            else:
                db.commit()
                db.close()
                return False
        except:
            db.rollback()

    def card_add(self, cardnumber):
        '''
        Registing a new ID card to parking system
        '''
        self.cardnumber = cardnumber
        
        db = mysql.connect(host = 'localhost', user = 'root', passwd ='HongMinh1960', db = 'parking',
	charset = 'utf8')
        cursor = db.cursor()
        
        query = "INSERT INTO card(cardnumber) VALUES({})".format(self.cardnumber)
        try:
            cursor.execute(query)
            db.commit()
            db.close()
        except:
            db.rollback()
            
        return print("Add card thành công")
        
    def card_del(self, cardnumber):
        """
        Delete a registed card from database
        """
        self.cardnumber = cardnumber
        
        db = sql.connect("parking.sql")
        query = "DELETE FROM card WHERE cardnumber = {}".format(self.cardnumber)
        db.execute(query)
        db.commit()
        db.close()
        return "Đã xóa card"

    
    
        
        
