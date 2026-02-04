from flask import Flask, render_template,request
from waitress import serve
from calculate import *

app = Flask(__name__)


@app.route("/",methods=['GET', 'POST'])
def hell():
    if request.method == 'POST':

        username = request.form.get("username")

        if len(username) <17:
            if doesPlayerExist(username):
                playtime = getPlaytime(username)
                shameText=shame(playtime)
                return render_template("main.html", player=username, hours=str(math.trunc(playtime/3600)),shame=shameText.split('\n'))
                # self documenting code
            else:
               return render_template("main.html", error="this fella never even joined mco") 
        else:
            return render_template("main.html", error="username cant be longer than 16 characters")
        
        if doesPlayerExist(username):
            return render_template("main.html", error="please input an username")


    return render_template("main.html")

# idk how this wsgi stuff works
serve(app, listen='*:8080')
