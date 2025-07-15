from flask import Flask, render_template, send_file, request
from scripts.parser import parse_logs
from scripts.geoip_map import generate_map
from scripts.pdf_report import generate_pdf
from scripts.virustotal import scan_url

app = Flask(__name__)

@app.route('/')
def index():
    ip_counts, cmd_counts = parse_logs()
    generate_map(ip_counts)
    return render_template('index.html', ip_counts=ip_counts, cmd_counts=cmd_counts)

@app.route('/report')
def report():
    ip_counts, cmd_counts = parse_logs()
    generate_pdf(ip_counts, cmd_counts)
    return send_file('static/honeypot_report.pdf')

@app.route('/vt', methods=['POST'])
def vt():
    url = request.form.get('url')
    result = scan_url(url)
    return result

if __name__ == '__main__':
    app.run(debug=True)
