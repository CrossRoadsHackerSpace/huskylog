#!/usr/bin/env python

import sqlite3
import configparser
import threading
import time
import curses
from curses import wrapper
from datetime import datetime, timezone

#clock called by threading to stay running in background
def update_time(stdscr):
    dims = stdscr.getmaxyx()
    while 1:
        date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        hour = datetime.now(timezone.utc).strftime("%H:%M:%S")
        stdscr.addstr(dims[0]-1, int(dims[1]/2)-12, 'Zulu: '+date+" "+hour)
        curses.noecho()
        curses.curs_set(0)
        stdscr.keypad(1)
        stdscr.refresh()
        time.sleep(1)

#define new callsign
def oper():
    oper = input('operator callsign: ')

#define location for use with lotw
#new qth
#adds new lotw location to database also
def nqth():
    mqth = input('operator location: ')

def powr():
    powr = input('operator tx power: ')

def setband():
    band = input('operator tx band: ')
    
def setmode():
    mode = input('operator tx band: ')

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

def lotw():
    print('lotw') #edits lotw table

def importfile():
    print('import')

def exportfile():
    print('export')

#open database by callsign stored in huskylog.conf
#create table if it does not exist
def connect2db():
    conn = sqlite3.connect(oper +'.db')
    db = conn.cursor()
    db.execute('''CREATE TABLE IF NOT EXISTS
    logbook(
    date TEXT,
    hour TEXT,
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
    )
    ''')
    db.close()

#display last 10 entries in database base
def tail():
    print('tail')
    b = sqlite3.connect('data/mydb')
    db.row_factory = sqlite3.Row
    cursor = db.cursor()
    cursor.execute('''SELECT date, hour, band, mode, call, srst, rrst, note FROM logbook''')
    for row in cursor:
        # row['name'] returns the name column in the query, row['email'] returns email column.
        print('{0} : {1}, {2}'.format(row['date'], row['hour'], row['band'], row['mode'], row['call'], row['srst'], row['rrst'], row['note']))
    db.close()

#read from database
def readdb():
    print('readdb')

#insert qso in database
def insert(n):
    db.execute('''INSERT INTO
        logbook VALUES(
        date TEXT,
        hour TEXT,
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
        )
        ''')

def display(stdscr):
    dims = stdscr.getmaxyx()
    stdscr.addstr(0, 0, 'Operator: ' + oper)
    stdscr.addstr(1, 0, 'Location: ' + mqth)
    stdscr.addstr(0, int(dims[1]/2)-4, 'Huskylog')
    stdscr.addstr(0, dims[1]-15, 'Power: ' + powr)
    stdscr.addstr(1, dims[1]-15, 'Band : ' + band)
    stdscr.addstr(2, dims[1]-15, 'Mode : ' + mode)
    stdscr.addstr(3, 0, 'Date')
    stdscr.addstr(3, 9, 'Time')
    stdscr.addstr(3, 17, 'Band')
    stdscr.addstr(3, 23, 'Mode')
    stdscr.addstr(3, 29, 'Callsign')
    stdscr.addstr(3, 40, 'SRST')
    stdscr.addstr(3, 45, 'RRST')
    stdscr.addstr(3, 51, 'Comments')
    stdscr.addstr(4, 0, '-' * dims[1])
    stdscr.addstr(dims[0]-2, 0, '-' * dims[1])
    stdscr.addstr(dims[0]-1, 0, '*Enter New Contact*')
    stdscr.addstr(dims[0]-1, dims[1]-36, 'Type .help for list of all commands')
    stdscr.move(dims[0]-3, 0)
    stdscr.refresh()

def display_help(stdscr):
    dims = stdscr.getmaxyx()
    stdscr.addstr(dims[0]-9, 0, '.oper <value> #? or new operator name')
    stdscr.addstr(dims[0]-8, 0, '.nqth <value> #? or new qth name')
    stdscr.addstr(dims[0]-7, 0, '.band <value> #? or in meters')
    stdscr.addstr(dims[0]-6, 0, '.powr <value> #? or power in watts')
    stdscr.addstr(dims[0]-5, 0, '.mode <value> #? or mode of operation')
    stdscr.addstr(dims[0]-3, 0, " " * dims[1])

#edit callsign in database
#if more than one, ask which one to edit and confirm
#option to delete entry in database and confirm
def edit(n):
    print('edit')

def action(buff):
    print('action')

#read huskylog.conf for settings
# if huskylog.conf is empty, prompt for fields and create it
config = configparser.ConfigParser()
config.read('huskylog.conf')

date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
hour = datetime.now(timezone.utc).strftime("%H:%M:%S")
oper = getdefault('oper')
mqth = getdefault('mqth')
powr = getdefault('powr')
band = getdefault('band')
mode = getdefault('mode')

connect2db()

def main (stdscr):
    display(stdscr)
    clock = threading.Thread(target=update_time, args=(stdscr,))
    clock.daemon = True
    clock.start()
    dims = stdscr.getmaxyx()
    buff = ""
    list = []
    while 1:
        char = stdscr.getkey()
        if char != " ":
            buff += char
            stdscr.addstr(dims[0]-3, 0, buff)
        if char == " ":
            list.append(buff)
        if buff == ".quit\n":
            break
        if buff == ".help\n":
            display_help(stdscr)
            buff = ""
        
        
wrapper(main)

writeconf()