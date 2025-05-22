import requests

def create_odoo_lead(name, email, phone, description):
    # Replace these with your Odoo credentials and URL
    ODOO_URL = "https://claimwiseadjuster.odoo.com"
    API_KEY = "61d7e0fda8e22c874ea94a95829a78103acbbacb"
    DB_NAME = "your-db"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "name": name,
        "email_from": email,
        "phone": phone,
        "description": description
    }
    response = requests.post(f"{ODOO_URL}/api/leads", json=data, headers=headers)
    return response.json()
