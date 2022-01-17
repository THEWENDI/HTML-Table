from cgi import print_environ_usage 
from flask import Flask, render_template  
app = Flask(__name__)    

@app.route('/')
def index():
    users_info = [
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
    return render_template("index.html", users = users_info)


# @app.route('/4')
# def numbox():
#     return render_template("index2.html")

# @app.route('/<int:col>/<int:row>/<string:color1>/<string:color2>')
# def colornumbox(col,row,color1,color2):
#     return render_template("index3.html",col= int(col/2),row=int(row/2),color1=color1,color2=color2)

# @app.route('/users/<username>/<id>')
# def show_user_profile(username, id):
#     print(username)
#     print(id)
#     return "username: " + username + ", id: " + id

if __name__=="__main__":   
    app.run(debug=True)    

