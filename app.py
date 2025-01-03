from flask import Flask, render_template, request, jsonify
from cve_service import get_cves, get_cve_details
import requests


app = Flask(__name__)

@app.route('/cves/list')
def cve_list():
    results_per_page = int(request.args.get('resultsPerPage', 10))
    page = int(request.args.get('page', 1))
    cves, total_records = get_cves(results_per_page, (page - 1) * results_per_page)
    return render_template('index.html', cves=cves, total_records=total_records, results_per_page=results_per_page, page=page)

@app.route('/cves/<cve_id>')
def cve_detail(cve_id):
    url = f"https://services.nvd.nist.gov/rest/json/cve/2.0/{cve_id}"
    try:
        response = requests.get(url)  # Use requests.get, not request.get
        if response.status_code == 200:
            data = response.json()
            return render_template('cve_detail.html', cve=data)
        else:
            return f"Error: Received status code {response.status_code} from the API"
    except requests.exceptions.JSONDecodeError:
        return "Error: Invalid JSON received from the API"
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == '__main__':
    app.run(debug=True)
