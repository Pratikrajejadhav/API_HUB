
import json, os
from datetime import datetime

class FileStorage:
    def __init__(self, base_dir="storage"):
        os.makedirs(base_dir, exist_ok=True)
        self.base_dir = base_dir

    def save(self, record):
        fname = datetime.utcnow().isoformat().replace(":","_") + ".json"
        with open(os.path.join(self.base_dir, fname),"w") as f:
            json.dump(record,f,indent=2)
