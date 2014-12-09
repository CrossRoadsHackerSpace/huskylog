import sqlite3 as lite
import configparser
import curses
import time

screen = curses.initscr()
curses.noecho()
dims = screen.getmaxyx()

#make sqlite database
def mkdb(n):
  with con:
    cur = con.cursor()    
    cur.execute("CREATE TABLE logbook(
      date TEXT, 
      time TEXT, 
      band TEXT, 
      mode TEXT, 
      call TEXT, 
      srst TEXT,
      rrst TEXT,
      note TEXT,
      oper TEXT,
      mqth TEXT,
      lotw TEXT,
      eqsl TEXT
      ")

# open last database by default stored in huskylog.conf
# if huskylog.conf is empty, prompt for fields and create it
def connect2db():
  config = configparser.ConfigParser()
  config.read('huskylog.conf')
  oper = ConfigSectionMap("Default")['oper']
  mqth = ConfigSectionMap("Default")['mqth']
 
  config['DEFAULT'] = {
    'oper': 
      'aa0na',
    'mqth': 
      'farm',
    }
  #con = lite.connect('%oper.db')
  

#define location for use with lotw
#new qth
def nqth():

#display last 10 entries in database base
def tail():  

#insert qso in database
def insert(n):  
  cur.execute("INSERT INTO logbook VALUES(
  date,
  time,
  band,
  mode,
  call,
  srst,
  rrst,
  note,
  mqth TEXT,
  lotw TEXT,
  eqsl TEXT 
  ")

#edit callsign in database
#if more than one,   ask which one to edit and   confirm
#option to delete entry   in database and   confirm
def edit(n):  

#connect2db()

#


curses.endwin()
