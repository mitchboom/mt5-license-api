from flask import Flask, request
import os
import sys

app = Flask(__name__)

# List of valid account numbers (as strings)
valid_accounts = [str(x) for x in ["7478389",            ## Mitch Test Server
                                   "664494",             ## Mitch VPS
                                   "660175",             ## Dave Account
                                   "51655118"]]

@app.route('/')
def home():
    return "MT5 License Server is running!"

@app.route('/validate', methods=['POST'])
def validate():
    account_no = request.form.get('account_no', '').strip().replace('\x00', '')
    
    print("🛠 Received POST request")
    sys.stdout.flush()

    print("Account number received:", repr(account_no))  # Shows hidden characters
    sys.stdout.flush()

    if account_no in valid_accounts:
        print("✅ License verified for", account_no)
        sys.stdout.flush()
        return "success"
    
    print("❌ Invalid license for", account_no)
    sys.stdout.flush()
    return "fail"

app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
