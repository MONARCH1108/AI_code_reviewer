from flask import Flask, render_template, request
from utils.functions import review_the_code

app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def main():
    response = ""
    if request.method == "POST":
        code = request.form.get("code")
        response = review_the_code(code)
    
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)