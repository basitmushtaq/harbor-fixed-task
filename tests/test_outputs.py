from pathlib import Path


import json
from pathlib import Path
def test_report_values():
    data = json.loads(Path("/app/report.json").read_text())
    assert data["total_requests"] == 6
    assert data["unique_ips"] == 3
    assert data["top_path"] == "/index.html"