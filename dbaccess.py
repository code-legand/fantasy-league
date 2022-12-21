"""
this module is used to perform operations on database
"""
import sqlite3
data=[]

#--------------returns the database object-----------------
def db_connect():
    path=__file__.replace('dbaccess.py', 'players.db')
    return sqlite3.connect(path)

#--------------returns the cursor object-------------------
def give_cursor():
    dbase_object=db_connect()
    return dbase_object.cursor()

#----------------read data from the tables-----------------
def read_data(command):
    cursor_object=give_cursor()
    cursor_object.execute(command)
    data=cursor_object.fetchall()
    return data

#-----------writing data to team table----------------
def write_data(team_name, players, points):
    dbase_object=db_connect()
    cursor_object=dbase_object.cursor()
    command='SELECT name from teams;'
    cursor_object.execute(command)
    data=cursor_object.fetchall()
    print(data)
    #print(team_name, players, points)
    if team_name in [x[0] for x in data]:
        dbase_object.close()
        return 2
    else:
        for i in range(len(players)):
            player=players[i]
            point=points[i]
            try:
                #print(team_name)
                #print(team_name, player, point)
                command="INSERT INTO teams(name, players, value) VALUES('{0}', '{1}', {2});".format(team_name, player, point)
                #print(command)
                cursor_object.execute(command)
                dbase_object.commit()
                
            except:
                dbase_object.rollback()
                dbase_object.close()
                return 0
            
        dbase_object.close()
        return 1
