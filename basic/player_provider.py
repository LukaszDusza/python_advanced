from player_model import Player
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="mydatabase")

mycursor = mydb.cursor()

def create_player(name, email):
    sql = "INSERT INTO users (name,email,points) values(%s, %s, %s)"
    values = (name,email, 0)
    mycursor.execute(sql, values)
    mydb.commit()
    print(mycursor.rowcount, "record inserted")
    return Player(name,email,0)

def del_player_from_db(player):
    # sql = "DELETE FROM users where email = %s"
    # value = player.email
    # mycursor.execute(sql, value)
    # mydb.commit()
    # print(mycursor.rowcount, "user" + player.get_name() +  " deleted")

    # zaimplementuj poprawnię tą definicję i skaskuj pass
    pass

def show_all_players():
    # mycursor.execute("USE mydatabase")
    mycursor.execute("SELECT * FROM users")
    for x in mycursor:
        print(x)