# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 13:40:53 2018

@author: quangtuan1412@gmail.com
"""
import serial
import sqlite3 as sql
import time
from threading import Thread # da luong
from modules.idcard2 import Card


if __name__ == "__main__":
            
    port = 'COM3'
    baudrate = 9600

    card = Card()

    cardnumber = ''

    START = True
    while START:
        cardnumber = card.read_card(port, baudrate)
        if cardnumber:
            print(cardnumber)
            if card.check_card(cardnumber):
                card.add_card(cardnumber)
            else:
                print("Lỗi: Card đã được đăng ký trong hệ thống")
        else:
            print("Waiting to read card....")
        
    print("Tổng cộng đã đọc được {} thẻ giữ xe".format(str(len(cardnumber))))
    for item in cardnumber:
        print(item)