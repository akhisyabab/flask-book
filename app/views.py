from flask import Flask, render_template, session, request, redirect, url_for, escape, blueprints
#from formregister import daftar

import sqlite3 as sql


from . import app

'''  if 'username' in session:
        username=session['username']
        return 'Logged in as ' + username + '<br>' + \
               "<b><a href='/logout'>click here to log out</a></b>"
    return "You are not logged in <br><a href='/login'></b>" + \
        "click here to log in</b></a>"
'''


#### blueprints ####

from app.home.views import home_blueprint
from app.users.views import users_blueprint
from app.members.views import members_blueprint
from app.my_api.views import api_blueprint
#from users import users as pengguna


# register the blueprints
app.register_blueprint(home_blueprint)
app.register_blueprint(users_blueprint)
app.register_blueprint(members_blueprint)
app.register_blueprint(api_blueprint)

#@app.route('/register')
#def new_student():
#   return render_template('register.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         nama = request.form['nama']
         password = request.form['password']
         email = request.form['email']
         hp = request.form['hp']

         with sql.connect("/home/ekowibowo/PycharmProjects/db/murid.db") as con:
            cur = con.cursor()

            cur.execute("INSERT INTO students (nama,password,email,hp) VALUES (?,?,?,?)",(nama,password,email,hp) )

            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"

      finally:
         return render_template("result.html",msg = msg)
         con.close()








#cara lain menggunakan routes
# app.register_blueprint(pengguna)
