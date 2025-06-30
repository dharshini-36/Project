from flask import Flask,request,render_template

app=Flask(__name__)

@app.route("/")
def invitation():
    return render_template("project1.html")
    
@app.route("/register",methods=['GET','POST'])
def form():
    if request.method=='POST':
        data={
        "name":request.form.get("name"),
        "email":request.form.get("email"),
       "phonenumber":request.form.get("phone"),
        "gender":request.form.get("gender"),
        "events":request.form.get("events"),
        }
        return render_template("project1result.html",data=data)
    return render_template("project1form.html")
if __name__=="__main__":
    app.run(debug=True)
    