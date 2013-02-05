#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys

class FGMySQLDB:

    def __init__(self):
        self.hostname = None
        self.userid = None
        self.password = None
        self.dbname = None
        self.conn = None
        self.cur = None
        self.data = None

    def dbinfo(self, hostname, userid, password, dbname):
        self.hostname = hostname
        self.userid = userid
        self.password = password
        self.dbname = dbname

    def connect(self):
        try:
            self.conn = mdb.connect(self.hostname, self.userid, self.password, self.dbname)
            self.cur = self.conn.cursor(cursorclass=mdb.cursors.DictCursor)
        except mdb.Error, e:
            print "Error %d: %s" % (e.args[0],e.args[1])
            sys.exit(1)
        
    def close(self):
        try:
            self.conn.close()
        except:
            pass
    
    def select(self, querystr):
        self.cur.execute(querystr)
        self.data = self.cur.fetchall()
        return self.data
