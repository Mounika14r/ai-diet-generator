from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
    diet_plan=None

    if request.method=="POST":
        goal=request.form["goal"]

        if goal=="weight_loss":
            diet_plan=["Oats","Vegetable Salad","Fruits","Soup"]

        elif goal=="muscle_gain":
            diet_plan=["Eggs","Chicken","Rice","Milk"]

        else:
            diet_plan=["Rice","Dal","Vegetables","Fruits"]

    return render_template("index.html", diet_plan=diet_plan)

if __name__=="__main__":
    app.run(debug=True)