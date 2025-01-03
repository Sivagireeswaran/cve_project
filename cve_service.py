import requests

BASE_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"

def get_cves(limit, offset):
    params = {
        "resultsPerPage": limit,
        "startIndex": offset,
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    cves = data.get("vulnerabilities", [])
    total_records = data.get("totalResults", 0)
    return cves, total_records

def get_cve_details(cve_id):
    response = requests.get(f"{BASE_URL}/{cve_id}")
    return response.json()
