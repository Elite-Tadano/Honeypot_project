import json
from collections import Counter
from datetime import datetime

def parse_logs(log_path='/home/cowrie/cowrie/var/log/cowrie/cowrie.log.2025-07-11'):
    ips = []
    commands = []

    with open(log_path, 'r') as f:
        for line in f:
            try:
                data = json.loads(line)
                if data.get('eventid') == 'cowrie.session.connect':
                    ips.append(data.get('src_ip'))
                elif data.get('eventid') == 'cowrie.command.input':
                    commands.append(data.get('input'))
            except json.JSONDecodeError:
                continue

    ip_counts = Counter(ips)
    cmd_counts = Counter(commands)
    return ip_counts, cmd_counts
