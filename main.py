import sqlite3 as lite
import configparser
import curses
import time

#make sqlite database
def mkdb(n):
  with con:
    cur = con.cursor()    
    cur.execute('''CREATE TABLE logbook(
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
      powr TEXT,
      lotw TEXT,
      eqsl TEXT
      ''')

#open last database by callsign stored in huskylog.conf
#con = lite.connect('%oper.db')
def connect2db():
  print('connect2db')

#define new callsign
def call():
  oper = input('operator callsign: ')

#define location for use with lotw
#new qth
#adds new lotw location to database also
def nqth():
  mqth = input('operator location: ')

def lotw():
  print('lotw') #edits lotw table 

def importfile():
  print('import')

def exportfile():
  print('export')

#display last 10 entries in database base
def tail():  
  print('tail')

#insert qso in database
def insert(n):  
  cur.execute('''INSERT INTO logbook VALUES(
    date TEXT,
    time TEXT,
    band TEXT,
    mode TEXT,
    call TEXT,
    srst TEXT,
    rrst TEXT,
    note TEXT,
    mqth TEXT,
    powr TEXT,
    lotw TEXT,
    eqsl TEXT 
    ''')

#edit callsign in database
#if more than one, ask which one to edit and confirm
#option to delete entry in database and confirm
def edit(n):  
  print('edit')

#read huskylog.conf for settings
# if huskylog.conf is empty, prompt for fields and create it
config = configparser.ConfigParser()
config.read('huskylog.conf')

def getdefault(value):
  confvalue = value
  try:
    value = config['DEFAULT'][confvalue]
  except:
    print( confvalue + '... not found in huskylog.conf')
    value = input('input value: ')
    config['DEFAULT'][confvalue] = value
  return value

def writeconf():
  with open('huskylog.conf', 'w') as configfile:
    config.write(configfile)

oper = getdefault('oper')
mqth = getdefault('mqth')
powr = getdefault('powr')
band = getdefault('band')

stdscr = curses.initscr()

def main(stdscr):
  dims = stdscr.getmaxyx()
  stdscr.addstr(0, 0, 'Operator: ' + oper)
  stdscr.addstr(1, 0, 'Location: ' + mqth)
  stdscr.addstr(0, int(dims[1]/2)-4, 'Huskylog')
  stdscr.addstr(0, dims[1]-15, 'Power: ' + powr)
  stdscr.addstr(1, dims[1]-15, 'Band : ' + band)
  stdscr.addstr(3, 0, 'Date     Time')
  stdscr.addstr(3, 15, 'Band')
  stdscr.addstr(3, 21, 'Mode')
  stdscr.addstr(3, 27, 'Callsign')
  stdscr.addstr(3, 38, 'SRST')
  stdscr.addstr(3, 43, 'RRST')
  stdscr.addstr(3, 49, 'Comments')
  stdscr.addstr(4, 0, '-' * dims[1])
  stdscr.addstr(dims[0]-2, 0, '-' * dims[1])
  stdscr.addstr(dims[0]-1, 0, '*Enter New Contact*')
  stdscr.addstr(dims[0]-1, dims[1]-36, 'Type .help for list of all commands')
  stdscr.move(dims[0]-3, 0)
  stdscr.refresh()
  stdscr.getkey()

main(stdscr)

writeconf()
curses.endwin()


