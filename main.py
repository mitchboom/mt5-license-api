from flask import Flask, request
import os

app = Flask(__name__)

valid_accounts = [str(x) for x in ["7478389", "87654321", "51655118"]]

@app.route('/')
def home():
    return "MT5 License Server is running!"

@app.route('/validate', methods=['POST'])
def validate():
    account_no = request.form.get('account_no', '').strip()
    print("🛠 Received POST request")
    print("Account number received:", account_no)

    if account_no in valid_accounts:
        print("✅ License verified for", account_no)
        return "success"
    print("❌ Invalid license for", account_no)
    return "fail"

app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
