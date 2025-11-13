# Importing dependencies
import requests
import time
import pandas as pd
from supabase import create_client, Client
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import logging
import random
import io

# Connection to database
url = "https://xxx.supabase.co"
key = "xxxx"
supabase: Client = create_client(url, key)

# Email credentials
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "ufuomajoy27@gmail.com"
SENDER_PASSWORD = "xxx"
ADMIN_EMAIL = "ufuoma.ejite@gmail.com"

# Logging setup
LOG_FILE = "email_logs.log"
logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")


# FETCHING THE QUOTE OF THE DAY
base_url = "https://zenquotes.io/api/today/"
MAX_RETRIES = 5

def get_daily_quote():
    for attempt in range(MAX_RETRIES):
        try:
            r = requests.get(base_url, timeout=60)
            r.raise_for_status()
            data = r.json()
            quote = f"“{data[0]['q']}” - {data[0]['a']}"
            logging.info("Fetched daily quote successfully.")
            return quote
        except requests.exceptions.RequestException:
            if attempt < MAX_RETRIES - 1:
                logging.warning(f"Connection error. Retrying")
                time.sleep(5)
            else:
                logging.error("Failed to connect after all retries.")
                return "FATAL ERROR: Failed to connect after all retries."
        except Exception:
            logging.error("Data received was invalid or malformed.")
            return "FATAL ERROR: Data received was invalid or malformed."


# FETCH SUBSCRIBERS DATA FROM THE DATABASE 
def get_subscribers():
    try:
        response = supabase.table("daily_quotes_subscribers").select("email", "first_name").execute()
        df = pd.DataFrame(response.data)
        logging.info(f"{len(df)} subscribers gotten from database.")
        return df
    except Exception as e:
        logging.error(f"Error fetching subscribers: {e}")
        return pd.DataFrame(columns=["email", "first_name"])


# EMAIL SENDING FUNCTION
def send_email(recipient_email, first_name, quote):
    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = recipient_email
    msg["Subject"] = "✨ Your Daily Quote ✨"

    body = f"Hi {first_name},\n\nHere’s your quote for today:\n\n{quote}\n\nHave a beautiful day!\n\n— Your Friend\nUfuomzy!"
    msg.attach(MIMEText(body, "plain", "utf-8"))

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
        logging.info(f"Email sent to {recipient_email}")
        return True
    except Exception as e:
        logging.error(f"Failed to send email to {recipient_email}: {e}")
        return False


# RETRY FUNCTION
def send_with_retry(email, first_name, quote, retries=3, delay=5):
    for attempt in range(1, retries + 1):
        success = send_email(email, first_name, quote)
        if success:
            return True
        logging.warning(f"Attempt {attempt} failed for {email}. Retrying in {delay}s...")
        time.sleep(delay)
    logging.error(f"All retries failed for {email}")
    return False


# SEND SUMMARY REPORT TO ADMIN

def send_summary_log():
    try:
        logging.info("Preparing to send summary log to admin...")

        # Ensure logs are flushed and closed before reading
        logging.shutdown()
        time.sleep(1)

        # Safely read log file
        with open(LOG_FILE, "r", encoding="utf-8", errors="replace") as f:
            log_content = f.read()

        msg = MIMEMultipart()
        msg["From"] = SENDER_EMAIL
        msg["To"] = ADMIN_EMAIL
        msg["Subject"] = "Daily Quote Email Summary Report"
        msg.attach(MIMEText(log_content, "plain", "utf-8"))

        # SMTP connection with handshake and retries
        for attempt in range(3):
            try:
                with smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=60) as server:
                    server.ehlo()
                    server.starttls()
                    server.ehlo()
                    server.login(SENDER_EMAIL, SENDER_PASSWORD)
                    server.send_message(msg)
                logging.info("Summary log sent to admin.")
                print("Summary email successfully sent to admin!")
                return
            except Exception as smtp_err:
                logging.warning(f"Attempt {attempt+1} to send summary failed: {smtp_err}")
                time.sleep(5)
        
        logging.error("All attempts to send summary log failed.")
        print("Summary log email failed after multiple attempts.")
    
    except Exception as e:
        logging.error(f"Unexpected failure while sending summary log: {e}")
        print(f"Unexpected failure while sending summary log: {e}")


# MAIN LOGIC
def main():
    logging.info("=== Daily Quote Email Process Started ===")
    quote = get_daily_quote()
    subscribers = get_subscribers()

    if subscribers.empty:
        logging.warning("No subscribers found.")
        return

    for _, row in subscribers.iterrows():
        email = row["email"]
        first_name = row.get("first_name")
        send_with_retry(email, first_name, quote)

    send_summary_log()
    logging.info("=== Daily Quote Email Process Completed ===")


if __name__ == "__main__":
    main()


