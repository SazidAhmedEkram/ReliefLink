````md
# ReliefLink – Disaster Relief & Shelter Management System

> A console-based Python application for managing disaster relief operations, including affected family registration, relief inventory, shelter allocation, and statistical reporting.

---

## 📖 Project Overview

Natural disasters such as floods, cyclones, and landslides affect thousands of families every year. Relief organizations often manage beneficiary information, relief supplies, and shelter allocation manually, which may lead to duplicate registrations, incorrect distributions, inventory shortages, and inefficient reporting.

**ReliefLink** is a console-based Disaster Relief Management System developed using **Python 3**, **NumPy**, and **JSON**. The system allows relief officers to register affected families, manage relief inventories, distribute relief packages, allocate shelters, and generate statistical reports for better decision-making.

---

## 🎯 Objectives

- Digitize disaster relief management.
- Prevent duplicate family registration and relief distribution.
- Maintain relief inventory efficiently.
- Allocate shelters based on available capacity.
- Generate useful statistical reports using NumPy.
- Store all information permanently using JSON.

---

## 👥 Target Users

- NGOs
- Relief Organizations
- Volunteers
- Disaster Management Teams
- Local Government Authorities

---

# 🛠 Technology Stack

- Python 3
- NumPy
- JSON
- Object-Oriented Programming (OOP)
- Console-Based Interface

---

# 📌 Features

## 1. Family Management

- Register affected families
- View all registered families
- Search family by ID, Name, or Phone
- Update family information
- Delete family records
- Prevent duplicate Family IDs
- Validate user inputs

---

## 2. Relief Inventory Management

Manage relief items including:

- Rice
- Water
- Blanket
- Medicine
- Baby Food
- Clothes
- Hygiene Kit

Operations

- Add Item
- View Inventory
- Update Quantity
- Delete Item
- Low Stock Warning

---

## 3. Shelter Management

Manage temporary shelters.

Features

- Add Shelter
- View Shelters
- Search Shelter
- Update Shelter
- Delete Shelter
- Allocate Family
- Remove Family
- Capacity Validation

---

## 4. Relief Distribution

- Search registered family
- Select relief package
- Distribute relief
- Automatically update inventory
- Prevent duplicate distribution
- Save distribution history

---

## 5. Reports

Generate reports including:

- Total Registered Families
- Families Served
- Families Waiting
- Families by District
- Families by Damage Level
- Remaining Inventory
- Shelter Occupancy
- Distribution History

---

## 6. Statistical Analysis (NumPy)

Calculate

- Average Family Size
- Maximum Family Members
- Minimum Family Members
- Total Affected People
- Percentage of Families Served
- High Priority Family Count
- Shelter Occupancy Rate
- Average Inventory Remaining

---

# 📂 Data Storage

All information is stored using JSON files.

```
data/
│
├── families.json
├── inventory.json
├── shelters.json
└── distribution.json
```

The application automatically loads existing data during startup and saves updated information before exiting.

---

# 📚 Data Structures Used

| Data Structure | Purpose |
|---------------|---------|
| List | Store families, shelters, inventory, distribution records |
| Tuple | Fixed values (Damage Levels, Package Types) |
| Set | Prevent duplicate relief distribution |
| Dictionary | Store record details as key-value pairs |

---

# 🏗 Object-Oriented Design

## Family

Attributes

- Family ID
- Head Name
- Phone
- District
- Village
- Members
- Damage Level
- Shelter Needed
- Relief Status

---

## InventoryItem

Attributes

- Item Name
- Quantity

---

## Shelter

Attributes

- Shelter ID
- Shelter Name
- District
- Capacity
- Occupied Seats

---

## Distribution

Attributes

- Family ID
- Distributed Items
- Quantity
- Date

---

## ReliefManager

Responsibilities

- Manage all modules
- Load and save JSON files
- Generate reports
- Coordinate application workflow

---

# 📋 Main Menu

```
=============================
RELIEFLINK MAIN MENU
=============================

1. Family Management
2. Relief Inventory
3. Shelter Management
4. Relief Distribution
5. Reports & Statistics
6. Save Data
7. Exit

Choose:
```

---

# 📁 Project Structure

```
ReliefLink/
│
├── main.py
├── manager.py
├── models.py
├── validation.py
├── file_handler.py
├── statistics.py
├── menu.py
├── utils.py
│
├── data/
│   ├── families.json
│   ├── inventory.json
│   ├── shelters.json
│   └── distribution.json
│
└── README.md
```

---

# ⚙ Workflow

```
Start Program
      │
Load JSON Files
      │
Display Main Menu
      │
Select Module
      │
Perform Operation
      │
Update Records
      │
Generate Reports (Optional)
      │
Save JSON Files
      │
Exit Program
```

---

# ⚠ Validation & Exception Handling

The system handles:

- Invalid menu choices
- Invalid numeric input
- Duplicate Family IDs
- Missing JSON files
- Empty JSON files
- Corrupted JSON data
- Negative quantities
- Shelter capacity overflow
- Invalid phone numbers

---

# 👨‍💻 Team Members & Responsibilities

## Sazid Ahmed Ekram (Project Lead)

- Overall project architecture
- Main menu and application flow
- ReliefManager implementation
- Module integration
- Git repository management
- Final testing
- Documentation & presentation

---

## Easha

### Family Management Module

Responsibilities

- Family class
- Add Family
- View Family
- Search Family
- Update Family
- Delete Family
- Input Validation
- Duplicate ID Prevention

---

## Borshon

### Inventory & Shelter Module

Responsibilities

- Inventory Management
- Shelter Management
- Shelter Allocation
- Capacity Validation
- Inventory CRUD

---

## Anurag

### File Handling & Statistics

Responsibilities

- JSON File Handling
- Exception Handling
- Report Generation
- Distribution History
- NumPy Statistical Analysis
- Data Persistence

---

# 🚀 Future Improvements

- Tkinter GUI Version
- QR Code Family Identification
- Role-Based Login System
- PDF Report Generation
- SMS Notification
- Barcode-Based Inventory
- Cloud Database Integration
- Mobile Application
- GIS Map Integration

---

# 📌 Course Learning Outcomes

This project demonstrates:

- Variables & Data Types
- Operators
- Conditional Statements
- Loops
- Functions
- Object-Oriented Programming
- Lists
- Tuples
- Sets
- Dictionaries
- JSON File Handling
- Exception Handling
- NumPy
- Modular Programming

---

# 📄 License

This project is developed solely for academic purposes as part of the **Programming in Python (Mid-Term Project)** course.

---

# ❤️ Acknowledgements

We sincerely thank our course instructor for providing the project guidelines and encouraging us to develop a practical solution using Python fundamentals.

---

**Project Name:** ReliefLink – Disaster Relief & Shelter Management System

**Course:** Programming in Python

**Semester:** Summer 2025–2026

**Version:** 1.0.0
````
