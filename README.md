# Cowrie Honeypot Intrusion Detection System

A real-world security project using [Cowrie](https://github.com/cowrie/cowrie) to simulate vulnerable SSH/Telnet services, capture attacker behavior, and analyze logs with a custom Flask dashboard, IP geolocation, Snort integration, and PDF reporting.

---

## Features

- SSH/Telnet honeypot with full interaction logging (via Cowrie)
- Real-time dashboard showing attacker IPs, commands, and alerts
- GeoIP visualization of attackers on an interactive world map
- VirusTotal integration to check malicious URLs
- PDF report generation for incident response teams

---

## Project Structure

```
cowrie-honeypot/
├── app.py # Flask web dashboard
├── scripts/ # Log parsers and integrations
│ ├── parser.py
│ ├── geoip_map.py
│ ├── pdf_report.py
│ └── virustotal.py
├── templates/ # HTML templates
│ ├── index.html
│ └── report_template.html
├── static/ # Static files like map output
│ └── map.html
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### 1. Install Dependencies

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

### 2. Setup Cowrie Honeypot
Follow the guide on Cowrie GitHub or use:
```
git clone https://github.com/cowrie/cowrie.git
cd cowrie
python3 -m venv cowrie-env
source cowrie-env/bin/activate
pip install -r requirements.txt
cp etc/cowrie.cfg.dist etc/cowrie.cfg
```
Edit etc/cowrie.cfg to set ports, logging paths, etc.

Start Cowrie:
```bash
bin/cowrie start
```
### 3. Run the Dashboard

```bash
python app.py
```

Then visit http://localhost:5000

