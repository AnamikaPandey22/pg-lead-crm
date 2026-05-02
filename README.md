# 🏠 PG Lead Management CRM

A lightweight, scalable CRM MVP designed for managing PG (Paying Guest) booking leads.
Built as part of a product-focused assignment to demonstrate system design, usability, and real-world workflows.

---

## 🚀 Features

### ✅ Lead Management

* Add, view, and manage leads
* Track source (Instagram, Website, Call, etc.)
* Assign leads to agents

### 🔄 Pipeline Tracking

* Lead stages:

  * New → Contacted → Visit Scheduled → Negotiation → Closed

### ⏰ Follow-up Reminder System

* Smart follow-up tracking:

  * 🔴 Overdue
  * 🟡 Due Today
  * 🟢 Upcoming

### 🔍 Search & Filter

* Search by name or phone
* Filter by:

  * Status
  * Priority (Hot/Warm/Cold)
  * Assigned agent

### 📊 Dashboard

* Total leads
* Closed leads
* Conversion rate
* Leads by status
* Upcoming follow-ups

---

## 🧠 Product Thinking

This CRM is designed specifically for **PG booking workflows**, focusing on:

* Lead conversion tracking
* Follow-up prioritization
* Agent accountability
* Simple, scalable structure

---

## 🛠️ Tech Stack

* **Frontend + Backend**: Streamlit
* **Database**: SQLite
* **Language**: Python

---

## 📁 Project Structure

```
crm-app/
│
├── app.py
├── database.py
├── utils.py
├── pages/
│   ├── 1_Dashboard.py
│   ├── 2_Leads.py
│   ├── 3_Add_Lead.py
│
├── data/
│   └── crm.db
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

```bash
git clone <your-repo-link>
cd crm-app
pip install -r requirements.txt
streamlit run app.py
```

---

## 🌟 Future Improvements

* Role-based access (admin/agent)
* Notifications for follow-ups
* Lead scoring using ML
* Deployment with cloud database

---

## 👩‍💻 Author

Built with a focus on real-world usability, scalability, and product thinking.
