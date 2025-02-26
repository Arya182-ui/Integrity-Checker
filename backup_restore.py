import os, shutil
from datetime import datetime
from config import BACKUP_DIR

def backup_file(file_path):
    os.makedirs(BACKUP_DIR, exist_ok=True)
    backup_name = f"{os.path.basename(file_path)}_{datetime.now().strftime('%Y%m%d%H%M%S')}"
    shutil.copy2(file_path, os.path.join(BACKUP_DIR, backup_name))
