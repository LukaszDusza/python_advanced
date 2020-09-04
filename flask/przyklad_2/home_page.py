from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'author': 'John Doe',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route("/home")
def home():
    return render_template('index.html', posts=posts)

if __name__ == "__main__":
      app.run(port=8080, debug=True) # odkomentuj
   # pass  # usuń/zakomentuj