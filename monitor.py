from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from logger import log_change, upload_to_supabase
from backup_restore import backup_file
from hash_utils import calculate_hash

class IntegrityHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            hash_value = calculate_hash(event.src_path)
            backup_file(event.src_path)
            log_change(event.src_path, "MODIFIED", hash_value)
            upload_to_supabase(event.src_path, hash_value, "MODIFIED")

def start_monitoring(path):
    observer = Observer()
    observer.schedule(IntegrityHandler(), path, recursive=True)
    observer.start()
    print(f"Monitoring started at {path}")
    observer.join()
