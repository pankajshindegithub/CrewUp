from flask import *
from models.user import *
from models.clientRequest import *
from models.collobrate import *
app = Flask(__name__)

app.secret_key = "your_secret_key_here" # 🔒 Change this to a strong, random key
# Route for the "mainpage" 
@app.route("/")
def hello_world():
    return render_template("index.html", user=session.get("user", {}))


# Route for the "signpage" 
@app.route("/sign",methods=['GET'])
def sign_in():
    return render_template("sign.html")


# Route for the "jionbuttonpage" 
@app.route("/join",methods=['GET'])
def join_in():
    return render_template("join.html")

# Route for the "programmingpage" 
@app.route("/programming",methods=['GET'])
def programming():
    return render_template("programming.html",user=session.get("user", {}))

# Route for the "graphicpage" 

@app.route("/graphic",methods=['GET'])
def graphic():
    return render_template("graphic.html",user=session.get("user", {}))


# Route for the "writingpage" 
@app.route("/writing",methods=['GET'])
def writing():
    return render_template("writing.html",user=session.get("user", {}))

# Route for the "digitalmarketingpage" 
@app.route("/digital marketing",methods=['GET'])
def digitalmarketing():
    return render_template("digital marketing.html",user=session.get("user", {}))





# Route for the "freelancerid programming page" 
@app.route("/freelancer",methods=['GET'])
def program_profile():
    return render_template("freelancerid.html",user=session.get("user", {}))

# Route for the "Graphicid page" 
@app.route("/graphicid",methods=['GET'])
def graphic_profile():
    return render_template("graphicid.html",user=session.get("user", {}))

# Route for the "Writingid page" 
@app.route("/writingid",methods=['GET'])
def writing_profile():
    return render_template("writingid.html",user=session.get("user", {}))

# Route for the "digitalmarketindid" page" 
@app.route("/digitalid",methods=['GET'])
def digital_profile():
    return render_template("digitalid.html",user=session.get("user", {}))


@app.route("/dashboard",methods=['GET'])
def dashboard():
    hire = getHire()
    collab = getCollab()
    return render_template("dashboard.html", hire=hire,collab=collab)
# ===========================================================================
#                                  Backend Apis
# ===========================================================================

@app.route("/add_user", methods=["POST"])
def add_user_route():
    data = request.form
    result = add_user(data)
    if "error" in result:
        return jsonify(result), 400
    return render_template("join.html",message=result)
    
@app.route("/user_login",methods=['POST'])
def login_user_route():
    data = request.form
    result = login(data)
    if "error" in result:
        return jsonify(result), 400
    session['user']= result['user']
    return render_template("index.html",user=session['user'])

@app.route("/hire", methods=["POST"])
def hire_freelancer():
    if 'user' in session:
        data = request.form 
        result = add_client_Request(data)
        session["last_hire"] = result 
        return redirect(url_for("hello_world"))  
        # return render_template("index.html", user=session['user'] or {}, result=result)
    return redirect(url_for("sign_in"))  

@app.route("/collaborate",methods=['POST'])
def collaborate_freelancer():
    if 'user' in session:
        data = request.form
        result = add_collab(data)
        return redirect(url_for("hello_world"))  
    return redirect(url_for("sign_in"))  

if __name__ == "__main__":
    app.run(debug=True)