from first_five import app
from flask import render_template

#Athlete page route
@app.route('/myfive')
def myfive():
    name = 'Top Five Athletes'
    athlete_dict = {1:'Tony Hawk', 2:'Sage Kotsenberg', 3: 'Michael Jordan', 4: 'Payton Manning', 5:'Patrick Kane'}
    return render_template('myfive.html',name=name, athlete_dict=athlete_dict)
#home page route
@app.route('/')
def home():
    return render_template('home.html')