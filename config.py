import os
from dotenv import load_dotenv

load_dotenv()

# Supabase Configuration
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# VirusTotal API Key
VIRUSTOTAL_API_KEY = os.getenv("VIRUSTOTAL_API_KEY")

# Backup Directory
BACKUP_DIR = "./backups"
