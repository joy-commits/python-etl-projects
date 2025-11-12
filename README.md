# python-etl-projects
This repository demonstrates how Python can be used across three data engineering and analysis tasks, ranging from data ingestion and analysis to reporting and workflow automation. Each project demonstrates practical problem-solving, automation, and data handling skills applied to real-world contexts.

---

## 🏠 Airbnb Data Analysis

**Overview:**
Exploratory analysis of Airbnb listings data to uncover pricing trends, room type performance, and host distribution patterns.

**Highlights:**

* Analyzed average price and availability by room type.
* Identified top hosts by number of listings.
* Used Python (Pandas, Matplotlib) for data wrangling and visualization.

**Sample Insight:**
Hotel rooms had the highest average price (~$310), while shared rooms were the most affordable (~$84).

---

## 💬 ZenQuotes Daily Automation

**Overview:**
A Python script that automatically fetches daily motivational quotes from the [ZenQuotes API](https://zenquotes.io) and sends them to subscribers via email.

**Highlights:**

* Uses `requests` for API integration.
* Includes retry logic for resilience.
* Sends daily emails via `smtplib`.
* Designed to log errors and maintain uptime.

**Outcome:**
A lightweight, fully automated inspiration service — reliable and low-maintenance.

---

## 🗄️ PostgreSQL Data Processing Automation

**Overview:**
An automation flow for reading data from a source PostgreSQL table (read-only) and staging it for further processing or analysis.

**Highlights:**

* Created a **staging table** to handle read-only source restrictions.
* Included logic to process and mark handled records.
* Designed for extensibility and compatibility with existing pipelines.

**Outcome:**
Improved workflow efficiency while maintaining data integrity and separation of concerns.

---

## ⚙️ Tech Stack

* **Tools:** Python, SQL, Task Scheduler
* **Concepts:** Data analysis, API automation, ETL, workflow design
