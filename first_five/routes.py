from first_five import app
from flask import render_template

#Athlete page route
@app.route('/myfive')
def myfive():
    athlete_dict = {1:'Tony Hawk', 2:'Sage Kotsenberg', 3: 'Michael Jordan', 4: 'Peyton Manning', 5:'Patrick Kane'}
    return render_template('myfive.html', athlete_dict=athlete_dict)
#home page route
@app.route('/')
def home():
    name = 'Top Five Athletes'
    return render_template('home.html',name=name)