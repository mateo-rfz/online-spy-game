from flask import (
        Flask,
        redirect , 
        request , 
        render_template , 
        make_response
        )




from modules import dbManager




app = Flask(__name__)








@app.route("/", methods = ["GET" , "POST"])
def main () :
    """
    main page for web site 
    """
    return render_template("home.html")








 


@app.route("/game/<string:gameId>")
def gameMng(gameId):
    existing_role = request.cookies.get(f"role_{gameId}")

    if existing_role:
        role = existing_role
    else:
        DB = dbManager.DbManager()
        role = DB.getAct(gameId)

    resp = make_response(render_template("releaseAct.html", gameId=gameId, role=role))

    if not existing_role:
        resp.set_cookie(f"role_{gameId}", role)

    return resp

















@app.route("/create_game", methods = ["GET", "POST"])
def createGame () :
    """
    route for create game 
    """
    if request.method == "POST" :
        playerNumbers = request.form.get("playerNumbers")
        spyNumbers = request.form.get("spyNumbers")
        
        DB = dbManager.DbManager()
        gameId = DB.addGame(int(playerNumbers) , int(spyNumbers))
        
        return render_template("gameInfo.html", gameId=gameId)
        
    else : 
        return render_template("createGame.html")









@app.route("/join_to_game", methods = ["GET" , "POST"])
def joinToGame () :
    """ 
    join to games it create by /create_game
    """
    if request.method == "POST" : 
        gameId = request.form.get("gameId")
        DB = dbManager.DbManager()
        act = DB.getAct(gameId)

        return redirect(f"/game/{gameId}")
    else : 
        return render_template("joinToGame.html")








@app.route("/about")
def about () :
    """
    about page
    """
    return render_template("about.html")




if __name__ == "__main__" : 
    app.run(host="0.0.0.0", debug=True)
