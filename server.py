from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = "Shhhh! Stay quiet!"

activities = []

@app.route("/")
def index():
    return render_template("index.html", activities=activities)

@app.route("/process_money", methods=["POST"])
def process_money():
    total_amount = session.get("total_amount", 0)
    
    if request.form['building'] == 'farm':
        gold_earned = random.randint(10, 20)
        total_amount += gold_earned
        activities.append(f"Earned {gold_earned} from the farm! ({datetime.now().strftime('%Y/%m/%d, %H:%M')})")
        
    if request.form['building'] == 'cave':
        gold_earned = random.randint(5, 10)
        total_amount += gold_earned
        activities.append(f"Earned {gold_earned} from the cave! ({datetime.now().strftime('%Y/%m/%d, %H:%M')})")
        
    if request.form['building'] == 'house':
        gold_earned = random.randint(2, 5)
        total_amount += gold_earned
        activities.append(f"Earned {gold_earned} from the house! ({datetime.now().strftime('%Y/%m/%d, %H:%M')})")
    
    if request.form['building'] == 'casino':
        gold_earned = random.randint(-50, 50)
        total_amount += gold_earned
        if gold_earned < 0:
            activities.append(f"Entered a casino and lost {-gold_earned} golds... Ouch... ({datetime.now().strftime('%Y/%m/%d, %H:%M')})")
        else:
            activities.append(f"Entered a casino and wins {gold_earned} golds!!! NAAAAASTY ({datetime.now().strftime('%Y/%m/%d, %H:%M')})")
    session["total_amount"] = total_amount
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)