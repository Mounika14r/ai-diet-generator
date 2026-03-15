from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
    diet_plan = None
    bmi = None
    category = None
    recommendation = None

    if request.method == "POST":
        age = int(request.form["age"])
        gender = request.form["gender"]
        weight = float(request.form["weight"])
        height_cm = float(request.form["height"])
        exercise = request.form["exercise"]
        goal = request.form["goal"]

        height_m = height_cm / 100  # convert to meters
        bmi = round(weight / (height_m ** 2), 1)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        exercise_rec = {
            "no_exercise":"Increase daily activity.",
            "once_week":"Try to exercise 3-4 times a week.",
            "twice_week":"Good, maintain consistency.",
            "daily":"Excellent, maintain your activity."
        }

        if goal == "weight_loss":
            diet_plan = {
                "Morning Breakfast":[
                    {"food":"Oats", "calories":150, "img":"oats.jpg"},
                    {"food":"Green Tea", "calories":30, "img":"green_tea.jpg"}
                ],
                "Afternoon Lunch":[
                    {"food":"Grilled Chicken", "calories":300, "img":"grilled_chicken.jpg"},
                    {"food":"Salad", "calories":100, "img":"salad.jpg"}
                ],
                "Evening Snacks":[
                    {"food":"Fruits", "calories":80, "img":"fruits.jpg"}
                ],
                "Night Dinner":[
                    {"food":"Vegetable Soup", "calories":120, "img":"vegetable_soup.jpg"},
                    {"food":"Brown Rice", "calories":200, "img":"brown_rice.jpg"}
                ]
            }
            recommendation = f"Reduce sugar and high-fat foods. Eat more fiber and protein. {exercise_rec[exercise]}"
        
        elif goal == "muscle_gain":
            diet_plan = {
                "Morning Breakfast":[
                    {"food":"Eggs", "calories":200, "img":"eggs.jpg"},
                    {"food":"Milk", "calories":150, "img":"milk.jpg"}
                ],
                "Afternoon Lunch":[
                    {"food":"Chicken Breast", "calories":350, "img":"chicken.jpg"},
                    {"food":"Rice", "calories":250, "img":"rice.jpg"}
                ],
                "Evening Snacks":[
                    {"food":"Nuts", "calories":150, "img":"nuts.jpg"}
                ],
                "Night Dinner":[
                    {"food":"Salmon", "calories":300, "img":"salmon.jpg"},
                    {"food":"Vegetables", "calories":100, "img":"vegetables.jpg"}
                ]
            }
            recommendation = f"Increase protein intake for muscle growth. {exercise_rec[exercise]}"
        
        else: # maintain health
            diet_plan = {
                "Morning Breakfast":[
                    {"food":"Daliya", "calories":180, "img":"daliya.jpg"},
                    {"food":"Fruits", "calories":80, "img":"fruits.jpg"}
                ],
                "Afternoon Lunch":[
                    {"food":"Rice", "calories":200, "img":"rice.jpg"},
                    {"food":"Dal", "calories":150, "img":"dal.jpg"},
                    {"food":"Vegetables", "calories":100, "img":"vegetables.jpg"}
                ],
                "Evening Snacks":[
                    {"food":"Buttermilk", "calories":50, "img":"buttermilk.jpg"},
                    {"food":"Nuts", "calories":150, "img":"nuts.jpg"}
                ],
                "Night Dinner":[
                    {"food":"Chapati", "calories":120, "img":"chapati.jpg"},
                    {"food":"Vegetables", "calories":100, "img":"vegetables.jpg"}
                ]
            }
            recommendation = f"Maintain balanced meals with proteins, carbs, and fats. {exercise_rec[exercise]}"

    return render_template("index.html",
                           diet_plan=diet_plan,
                           bmi=bmi,
                           category=category,
                           recommendation=recommendation,
                           age=age if request.method=="POST" else None,
                           gender=gender if request.method=="POST" else None,
                           exercise=exercise if request.method=="POST" else None)

if __name__ == "__main__":
    app.run(debug=True)