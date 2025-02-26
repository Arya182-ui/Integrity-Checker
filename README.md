# 🛡️ Integrity Checker

## 🔍 Overview
**Integrity Checker** is a Python-based tool that verifies file integrity by generating and comparing hash values.  
It ensures files are untampered by monitoring changes and providing real-time alerts.

---

## 🚀 Features
- ✅ **Multi-Hash Support**: MD5, SHA256, and SHA512.  
- 📊 **Advanced Logging & Reports**: Logs in CSV/JSON, Supabase database integration, and automated PDF reports.  
- 🕵️ **Enhanced Security**: Digital signatures, encryption, and rootkit detection.  
- ⏲️ **Smart Monitoring**: Real-time directory monitoring with priority alerts.  
- 📈 **Visualization**: Interactive dashboards with heatmaps for file change trends.  
- 🛡️ **Backup & Restore**: Auto-backup and file rollback on tampering.  
- 🌐 **Cross-Platform**: Supports Windows, macOS, and Linux.

---

## 🛠️ Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/integrity-checker.git
   cd integrity-checker

2. **Install dependencies**

```bash
pip install -r requirements.txt

```

3. **Configure environment variables**

Create a .env file:

```bash
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USER=your_email@gmail.com
EMAIL_PASSWORD=your_password
SLACK_TOKEN=your_slack_bot_token
SLACK_CHANNEL= #your_channel
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
```

## 📦 Usage

**🔑 Calculate Hashes**
```bash
python hash_calculator.py --file path/to/your/file.txt
```

**🕒 Start Monitoring**
```bash
python monitor.py --dir path/to/watch --email user@example.com
```

**📢 Send Notification**
```python
from notifier import notify_all
notify_all("File 'example.txt' changed!", level="CRITICAL", recipient_email="user@example.com")
```

**🧩 Project Structure**
```bash
📁 integrity-checker
├── config.py           # Configuration settings
├── hash_calculator.py  # Hash generation
├── monitor.py          # File & directory monitoring
├── notifier.py         # Notification system
├── backup.py           # Auto backup & restore
├── visualizer.py       # Data visualization
├── requirements.txt    # Dependencies
└── README.md           # Documentation
```

## **🔔 Alerts & Reports**

**Notifications**: Console, Email, Slack with priority levels (Info, Warning, Critical)
**Reports**: Weekly automated PDF summaries

## ☕ Support Me

Do you like My projects? You can show your support by buying me a coffee! Your contributions motivate me to keep improving and building more awesome projects. 💻❤  
[![Buy Me a Coffee](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](http://buymeacoffee.com/Arya182)


## **👥 Contributors**

**Ayush Gangwar** - Developer

Open to contributions! 🤝
