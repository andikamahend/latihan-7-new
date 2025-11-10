from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def beranda():
    return render_template('index.html')

@app.route('/profil')
def profil():
    return "Ini adalah halaman profil."

@app.route('/user/<username>')
def show_user_profile(username):
    return render_template('showuser.html', username=username)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nama = request.form['Nama']
        return render_template('index.html', nama=nama)
    
    return render_template('login.html')
if __name__ == '__main__':
    app.run(debug=False)