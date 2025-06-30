from flask import Flask,request,render_template
app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def form():
    if request.method=='POST':
        data={
        "uname":request.form.get("uname"),
        "email":request.form.get("email"),
        "comment":request.form.get("comment"),
        }
        return render_template("result_p2.html",data=data)
    return render_template("query.html")
if __name__=='__main__':
    app.run(debug=True)
    