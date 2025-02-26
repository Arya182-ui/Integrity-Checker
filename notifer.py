import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from config import EMAIL_HOST, EMAIL_PORT, EMAIL_USER, EMAIL_PASSWORD, SLACK_TOKEN, SLACK_CHANNEL

# Slack client initialization
slack_client = WebClient(token=SLACK_TOKEN)

def send_console_notification(message, level="INFO"):
    icons = {"CRITICAL": "🚨", "WARNING": "⚠️", "INFO": "ℹ️"}
    print(f"{icons.get(level, 'ℹ️')} [{level}] {message}")

def send_email_notification(subject, body, recipient):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_USER
    msg['To'] = recipient
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASSWORD)
            server.send_message(msg)
        print(f"✅ Email sent to {recipient}")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

def send_slack_notification(message):
    try:
        slack_client.chat_postMessage(channel=SLACK_CHANNEL, text=message)
        print("✅ Slack notification sent")
    except SlackApiError as e:
        print(f"❌ Slack error: {e.response['error']}")

def notify_all(message, level="INFO", recipient_email=None):
    send_console_notification(message, level)
    if recipient_email:
        send_email_notification(f"[{level}] File Integrity Alert", message, recipient_email)
    send_slack_notification(f"[{level}] {message}")
