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

 









@app.route("/<string:gamePath>")
def gameMng (gamePath) : 
    return gamePath













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
    return render_template("about.html")




if __name__ == "__main__" : 
    app.run(host="0.0.0.0", debug=True)
