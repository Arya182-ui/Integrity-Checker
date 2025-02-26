# This file is for a small Integrity Checker if you want just see how it works or you just want to try then you should use this 

import hashlib
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import os
import logging
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import config

# 📊 Setup Logging
if not os.path.exists('logs'):
    os.makedirs('logs')
logging.basicConfig(filename='logs/integrity_log.txt', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# 📧 Email Alert
def send_email_alert(file_path):
    msg = MIMEMultipart()
    msg['From'] = config.EMAIL_SENDER
    msg['To'] = config.EMAIL_RECEIVER
    msg['Subject'] = f"⚠️ Integrity Alert: {os.path.basename(file_path)} Changed"

    body = f"Alert: The integrity of '{file_path}' has been compromised!"
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP(config.SMTP_SERVER, config.SMTP_PORT) as server:
            server.starttls()
            server.login(config.EMAIL_SENDER, config.EMAIL_PASSWORD)
            server.send_message(msg)
        print(f"[✅] Email alert sent for {file_path}")
    except Exception as e:
        print(f"[❌] Failed to send email: {e}")

# 🔒 Hash Calculation
def calculate_hash(file_path, algorithm='sha256'):
    hash_func = getattr(hashlib, algorithm)()
    try:
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b''):
                hash_func.update(chunk)
        return hash_func.hexdigest()
    except FileNotFoundError:
        print(f"[!] File not found: {file_path}")
        return None

# 🔍 Hash Comparison
def compare_hash(file_path, expected_hash, algorithm='sha256'):
    file_hash = calculate_hash(file_path, algorithm)
    if file_hash:
        logging.info(f"Compared {file_path} | Expected: {expected_hash} | Got: {file_hash}")
        return file_hash == expected_hash
    return False

# 🕵️ Integrity Monitoring
def monitor_files(file_list, interval=30):
    print("\n🔍 Monitoring started... Press Ctrl+C to stop.")
    previous_hashes = {file: calculate_hash(file) for file in file_list}

    try:
        while True:
            for file in file_list:
                current_hash = calculate_hash(file)
                if current_hash != previous_hashes[file]:
                    print(f"[⚠️] Change detected in: {file}")
                    logging.warning(f"Integrity change detected in {file}")
                    send_email_alert(file)
                    previous_hashes[file] = current_hash
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\n[🔒] Monitoring stopped.")

# 🖥️ GUI (Tkinter)
def gui_interface():
    window = tk.Tk()
    window.title("🛡️ Integrity Checker")
    window.geometry("400x300")

    def select_file():
        return filedialog.askopenfilename()

    def calc_hash_gui():
        file_path = select_file()
        algo = simpledialog.askstring("Algorithm", "Enter algorithm (md5/sha256/sha512):")
        hash_val = calculate_hash(file_path, algo)
        if hash_val:
            messagebox.showinfo("Hash Result", f"{algo.upper()} Hash:\n{hash_val}")

    def compare_hash_gui():
        file_path = select_file()
        expected = simpledialog.askstring("Expected Hash", "Enter the expected hash:")
        algo = simpledialog.askstring("Algorithm", "Algorithm used (md5/sha256/sha512):")
        if compare_hash(file_path, expected, algo):
            messagebox.showinfo("Result", "✅ Hash matches!")
        else:
            messagebox.showwarning("Result", "❌ Hash mismatch!")

    def monitor_files_gui():
        files = filedialog.askopenfilenames()
        interval = simpledialog.askinteger("Interval", "Monitoring interval (seconds):", minvalue=5)
        monitor_files(list(files), interval)

    tk.Button(window, text="🧮 Calculate Hash", command=calc_hash_gui, width=25).pack(pady=10)
    tk.Button(window, text="🔍 Compare Hash", command=compare_hash_gui, width=25).pack(pady=10)
    tk.Button(window, text="🕵️ Monitor Files", command=monitor_files_gui, width=25).pack(pady=10)
    tk.Button(window, text="❌ Exit", command=window.quit, width=25).pack(pady=10)

    window.mainloop()

# 🏃 Entry Point
if __name__ == "__main__":
    print("=== 🛡️ Integrity Checker with Alerts & GUI ===")
    choice = input("Run in GUI mode? (y/n): ").lower()
    gui_interface() if choice == 'y' else monitor_files([input("Enter file path: ")], 30)
