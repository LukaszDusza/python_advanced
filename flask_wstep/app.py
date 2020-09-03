# to zaimportuj przed odpaleniem pliku
# python -m pip install --upgrade pip
# python -m pip install flask
# python -m pip install flask-mysql

from flask import Flask, render_template, json, request
from flaskext.mysql import MySQL
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

 # konfiguracja bazy danych   
app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_PASSWORD"] = "root"
app.config["MYSQL_DATABASE_DB"] = "mydatabase"
app.config["MYSQL_DATABASE_HOST"] = "localhost"
mysql = MySQL(app)

# tutaj dzieje się magia :) mianowicie, 
# Flask uruchamia serwer, który bedzie nasłuchiwał na pewnym porcie 
# i jesli otrzyma z przeglądarki request o metodzie GET http://localhost:5000/
# to ma kierować na ten url "/"

# dekorator albo adnotacja
@app.route("/", methods=["GET"])
def main():
    data = select_all_from_db()
    return render_template("index.html", data = data)

@app.route("/cars", methods=["GET"])
def get_all_cars():
    return select_all_from_db()

@app.route("/register-car", methods=["POST"])
def register_car():
    try:
        _brand = request.form['brand']
        _model = request.form['model']
        _color = request.form['color']
        print(_brand, _model, _color)
        insert_car_to_db(_brand, _model, _color)
        # return render_template("index.html")
        return json.jsonify(brand = _brand, model = _model, color = _color)
    except Exception as e:
        return json.dumps({'error': str(e)})
    
def check_data_base():
    cursor = mysql.connect().cursor()
    query = "drop table if exists cars"
    cursor.execute(query)

    query = "create table cars(id INT AUTO_INCREMENT PRIMARY KEY, brand varchar(30) null, model varchar(30) null, color varchar(30) null)"
    cursor.execute(query)

def insert_car_to_db(brand, model, color):
    conn =  mysql.connect()
    cursor = conn.cursor()
    sql = "insert into cars (brand,model,color) values(%s, %s, %s)"
    values = (brand,model,color) 
    cursor.execute(sql, values)
    conn.commit()
    print(cursor.rowcount, "record inserted")

def select_all_from_db():
    conn =  mysql.connect()
    cursor = conn.cursor()
    sql = "select brand, model, color from cars"
    cursor.execute(sql)
    row_headers=[x[0] for x in cursor.description] #this will extract row headers
    rv = cursor.fetchall()
    json_data=[]
    for result in rv:
        json_data.append(dict(zip(row_headers,result)))
    return json.dumps(json_data)
    
# ten kod musi byc na dole, bo nic poniżej nie zostanie skompilowanie
if __name__ == "__main__":
    # check_data_base()
    app.run(port=8080, debug=True)