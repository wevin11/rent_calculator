from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    income = request.form.get('income')  # Get the income value
    frequency = request.form.get('frequency')  # Get the selected frequency (monthly or yearly)
    debt_payments = request.form.get('debtPayments', 0)  # Get car payment, default to 0 if not provided

    try:
        income = float(income)  # Convert the income to a float
       
        if not debt_payments:
            debt_payments = 0
        else:
            debt_payments = float(debt_payments)
       
        # Adjust income based on the selected frequency
        if frequency == "yearly":
            income /= 12  # Convert yearly income to monthly income

        # Subtract the car and credit card payments from the income
        adjusted_income = income - (debt_payments)

        # Calculate affordable rent based on 30% of the adjusted income
        affordable_rent = adjusted_income * 0.3

        return jsonify({"rent": round(affordable_rent, 2)})

    except ValueError:
        return jsonify({"error": "Invalid input. Please enter valid amounts."}), 400

if __name__ == '__main__':
    app.run(debug=True)
