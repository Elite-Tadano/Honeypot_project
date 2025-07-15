from weasyprint import HTML
from jinja2 import Environment, FileSystemLoader
import os

def generate_pdf(ip_counts, cmd_counts, output_path='static/honeypot_report.pdf'):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('report_template.html')
    html_out = template.render(ip_counts=ip_counts.most_common(10), cmd_counts=cmd_counts.most_common(10))
    HTML(string=html_out).write_pdf(output_path)
