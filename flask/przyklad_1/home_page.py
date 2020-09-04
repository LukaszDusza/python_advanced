from flask import Flask, render_template

app = Flask(__name__)

''' @app.route to dekorator (adnotacja), która uruchamia metodę, do której przynależy.
    W poniższym przypadku, gdy wywołasz http://localhost:8080/home
    pojawi się strona index.html w przeglądarce.
    Stanie się tak, ponieważ @app.route przekierowało twoje zapytanie o treści "/home"
    na odpowiednik metody reprezentującej tą ścieżkę, czyli 'home_page()'
'''


@app.route("/home", methods=["GET"])
def home_page():
    return render_template("index.html")


@app.route("/about", methods=["GET"])
def about_page():
    return
    '''
    <h1> To jest about page </h1>
    '''


''' Poniższy warunek wykona się tylko wówczas, gdy plik flask_demo.py zostanie uruchomiony bezpośrednio.
    Jeśli plik ten zostanie uruchomiony pośrednio (np. przez zaimportowanie go w innym module) wówczas jego nazwa
    będzie inna niż __main__
'''

''' Poniższy zapis wewnątrz warunku if, konfiguruje start naszej aplikacji flask.
    Ustawiamy debug na włączony, oraz ustawiamy port, na którym nasłuchuje aplikacja.
'''
if __name__ == "__main__":
    app.run(port=8080, debug=True)  # odkomentuj
# pass                              # usuń/zakomentuj

''' UWAGA   Aby uruchomić tą aplikację musisz skopiować cały kod i przenieść do dowolnego pliku Python.
    Stwórz plik np. python_demo.py i skopiój cały kod.
    W tej samej lokalizacji stwórz folder 'templates' i dodaj tam plik 'index.html'
'''
