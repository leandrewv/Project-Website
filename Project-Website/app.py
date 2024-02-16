from flask import Flask, render_template,request,url_for,session,redirect
app = Flask(__name__)
app.secret_key = '123'



user_password={}


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/resultat', methods=['POST'])
def resultat():
    

    result=request.form
    n= result['username']
    p = result ['password']
    if n in user_password and user_password[n]== p :
        session['username'] = n
        return render_template('moto1.html', username=n, password=p)
    else:
        return render_template('pasdecompte.html')

@app.route('/addUser', methods=['POST'])
def register():
    

    result=request.form
    n = result['username']
    p = result['password']
    user_password[n] = p
    session['username'] = n
    return render_template('moto1.html',username=n, password=p)

@app.route('/moto1')
def moto1():
    if 'username' in session:
        username = session['username']
        return render_template('moto1.html', username=username)
    else:
        return redirect(url_for('login'))

@app.route('/login')
def login():
    return render_template('index.html')

@app.route('/equipe')
def equipe():
    return render_template('equipe.html')

@app.route('/modelselect')
def modelselect():
    return render_template('modelselect.html')





app.run(debug=True)


