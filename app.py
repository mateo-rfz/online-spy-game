from re import A
from flask import (
        Flask , 
        request , 
        render_template
        )





app = Flask(__name__)




@app.route("/", methods = ["GET" , "POST"])
def main () :
    """
    main page for web site 
    """
    pass





@app.route("/{gamePath}")
def gameMng (gamePath) : 
    pass







@app.route("/create_game", methods = ["GET" , "POST"])
def createGame () :
    """
    route for create game 
    """
    if request.methods == "POST" :
        gameName = request.form.get("gameName")
        playerNumbers = request.form.get("playerNumbes")
        
    else : 
        return render_template("createGame.html")









@app.route("/join_to_game", methods = ["GET" , "POST"])
def joinToGame () :
    """ 
    join to games it create by /create_game
    """
    pass



@app.route("/about")
def about () :
    """
    about page
    """
    pass




if __name__ == "__main__" : 
    app.run(host="0.0.0.0", debug=True)
