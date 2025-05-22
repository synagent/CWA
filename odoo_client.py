import requests

def create_odoo_lead(name, email, phone, description):
    # TEMPORARY - Disable actual request
    print("Mock Odoo lead creation:")
    print(f"Name: {name}, Email: {email}, Phone: {phone}, Description: {description}")
    return {"status": "ok", "msg": "Lead creation skipped for now"}

    # UNCOMMENT AND UPDATE WHEN READY:
    # ODOO_URL = "https://your-odoo-url.odoo.com"
    # API_KEY = "your-api-key"
    # headers = {
    #     "Authorization": f"Bearer {API_KEY}",
    #     "Content-Type": "application/json"
    # }
    # data = {
    #     "name": name,
    #     "email_from": email,
    #     "phone": phone,
    #     "description": description
    # }
    # response = requests.post(f"{ODOO_URL}/api/leads", json=data, headers=headers)
    
    # try:
    #     return response.json()
    # except Exception as e:
    #     print("ODoo API Error:", response.text)
    #     return {"error": "Odoo API failed", "details": str(e)}
