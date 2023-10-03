from flask import Flask,render_template,request
app = Flask(__name__)
@app.route("/")

def home():
    name = input("please enter your name ")
    return render_template("home.html",data={"name":name})
@app.route("/about",methods=['POST','GET'])
def about():
    if request.method=="POST":
        num1=int(request.form['num1'])
        num2=int(request.form['num2'])
        result=num1+num2
    
        return render_template("about.html",result={"result":result})
    else:
        return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)