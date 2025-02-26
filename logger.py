import csv, json
from datetime import datetime
from supabase import create_client
from config import SUPABASE_URL, SUPABASE_KEY

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def log_change(file_path, change_type, hash_value):
    log_data = {
        "timestamp": datetime.now().isoformat(),
        "file_path": file_path,
        "change_type": change_type,
        "hash": hash_value
    }

    with open("logs.csv", "a", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=log_data.keys())
        writer.writerow(log_data)

    with open("logs.json", "a") as jsonfile:
        json.dump(log_data, jsonfile)
        jsonfile.write('\n')

def upload_to_supabase(file_path, hash_value, change_type):
    data = {
        "file_path": file_path,
        "hash": hash_value,
        "change_type": change_type,
        "timestamp": datetime.now().isoformat()
    }
    supabase.table("file_integrity").insert(data).execute()
