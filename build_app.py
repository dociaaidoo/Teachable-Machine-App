"""Builds index.html with the exported Teachable Machine model embedded,
so the app opens with a double-click (no server needed)."""
import base64
import json
from pathlib import Path

here = Path(__file__).parent
model = json.loads((here / "model/model.json").read_text())
metadata = json.loads((here / "model/metadata.json").read_text())
weights = base64.b64encode((here / "model/weights.bin").read_bytes()).decode()

html = (here / "template.html").read_text()
html = html.replace("__MODEL__", json.dumps(model))
html = html.replace("__METADATA__", json.dumps(metadata))
html = html.replace("__WEIGHTS__", weights)
(here / "index.html").write_text(html)
print("wrote index.html", len(html) // 1024, "KB")
