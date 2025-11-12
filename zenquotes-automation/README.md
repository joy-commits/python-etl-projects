## 💌 ZenQuotes Daily Email Automation

This project automates fetching daily motivational quotes from the **ZenQuotes API**, delivering them via email to subscribers, and logging each delivery for monitoring and reliability. It demonstrates how Python can be used to combine APIs, automation, and email services efficiently.

### 📋 Project Overview

The goal of this automation is to:
* Retrieve a daily quote from the **ZenQuotes API**.
* Send personalized emails containing the quote to a list of recipients.
* Log delivery status for both subscribers and the admin.
* Ensure resilience with retries and error handling in case of API or network failures. <br>

This helps maintain consistent, automated email delivery without manual intervention.

---

### ⚙️ Workflow Summary

1. **Quote Retrieval**: 
   The script calls the ZenQuotes API (`https://zenquotes.io/api/today/`) to fetch the daily quote.

2. **Email Composition and Delivery**: 
   Using Python’s `smtplib`, it formats and sends the email to each subscriber.
   The admin receives a daily summary of delivery logs.

3. **Logging & Error Handling**: 
   Each run logs the success or failure of email delivery.
   The script retries API calls automatically if a request fails.


## 🧰 Tools

* **Python** – Core scripting language for fetching the quotes from the ZenQuotes API, sending the automated emails, formatting the message content and tracking delivery.
* **Task scheduler** – For scheduling the execution of the `.py` file.

---

## 🚀 How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/zenquotes-automation.git
   ```
2. Navigate to the project folder:

   ```bash
   cd zenquotes-automation
   ```
3. Install dependencies:

   ```bash
   pip install requests
   ```
4. Configure your email credentials and recipient list inside the script.
5. Run the automation:

   ```bash
   python zenquotes_api.py
   ```

---

## 🧩 Example Output

**Daily Quote Example:**

<img width="619" height="221" alt="daily_quote" src="https://github.com/user-attachments/assets/0a15a82a-9c64-4590-bd6e-e87f8e05edc2" />


**Email Log Example:**

<img width="1132" height="567" alt="logs" src="https://github.com/user-attachments/assets/096e0aeb-abb9-42fd-98e5-06d6ce4704d4" />


