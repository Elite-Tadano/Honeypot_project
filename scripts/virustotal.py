import requests

API_KEY = "b7d91a6846095fea640858714a77a3a4b3dbd785cf2c186bfede5a86b4f5eab4"

def scan_url(url):
    headers = {"x-apikey": API_KEY}
    data = {"url": url}
    response = requests.post("https://www.virustotal.com/api/v3/urls", data=data, headers=headers)
    
    if response.status_code == 200:
        result = response.json()
        analysis_id = result["data"]["id"]
        report = requests.get(f"https://www.virustotal.com/api/v3/analyses/{analysis_id}", headers=headers)
        return report.json()
    else:
        return {"error": "Failed to scan"}
