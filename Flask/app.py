from flask import Flask,render_template



app = Flask(__name__)
@app.route('/')
def Home():
    ToDO=["ჭამა","მეცადინეობა","თამაში","სახლის დალაგება", "ძილი"]
    return render_template('index.html', todo=ToDO)

@app.route('/ragaca')
def add_flask():
    return render_template('add_flask.html')



if __name__ == '__main__':
    app.run(debug=True)
