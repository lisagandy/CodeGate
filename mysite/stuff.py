import MySQLdb as mdb

con = mdb.connect('localhost','root','stuff0645','CODEGATE')
print con
con.close()

