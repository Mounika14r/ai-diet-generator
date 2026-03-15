from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
    diet_plan=None

    if request.method=="POST":
        goal=request.form["goal"]

        if goal=="weight_loss":
            diet_plan=["Oats","Salad","Fruits","Vegetables"]
        elif goal=="muscle_gain":
            diet_plan=["Eggs","Rice","Paneer","Milk"]
        else:
            diet_plan=["Balanced diet","Fruits","Rice","Vegetables"]

    return render_template("index.html", diet_plan=diet_plan)

if __name__=="__main__":
    app.run(debug=True)