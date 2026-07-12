# ReliefLink – Disaster Relief & Shelter Management System

**ReliefLink** is a console-based Python application for managing disaster relief operations, including affected family registration, relief inventory, shelter allocation, and statistical reporting.

## Project Overview

Natural disasters such as floods, cyclones, and landslides affect thousands of families every year. Relief organizations often manage beneficiary information, relief supplies, and shelter allocation manually, which can lead to duplicate registrations, incorrect distributions, inventory shortages, and inefficient reporting.

ReliefLink helps solve these problems by providing a simple command-line system that stores data in JSON files and uses NumPy for basic analysis.

## Objectives

* Digitize disaster relief management
* Prevent duplicate family registration and relief distribution
* Maintain relief inventory efficiently
* Allocate shelters based on available capacity
* Generate useful statistical reports using NumPy
* Store all information permanently using JSON files

## Target Users

* NGOs
* Relief organizations
* Volunteers
* Disaster management teams
* Local government authorities

## Technologies Used

* Python 3
* NumPy
* JSON
* Object-Oriented Programming (OOP)
* Console-based interface

## Features

### Family Management

* Register affected families
* View all registered families
* Search family by ID, name, or phone
* Update family information
* Delete family records
* Prevent duplicate Family IDs
* Validate user inputs

### Relief Inventory Management

Manage relief items such as:

* Rice
* Water
* Blanket
* Medicine
* Baby food
* Clothes
* Hygiene kit

Operations:

* Add item
* View inventory
* Update quantity
* Delete item
* Low stock warning

### Shelter Management

* Add shelter
* View shelters
* Search shelter
* Update shelter
* Delete shelter
* Allocate family
* Remove family
* Validate capacity

### Relief Distribution

* Search registered family
* Select relief package
* Distribute relief
* Automatically update inventory
* Prevent duplicate distribution
* Save distribution history

### Reports

Generate reports including:

* Total registered families
* Families served
* Families waiting
* Families by district
* Families by damage level
* Remaining inventory
* Shelter occupancy
* Distribution history

### Statistical Analysis

Using NumPy, the system can calculate:

* Average family size
* Maximum family members
* Minimum family members
* Total affected people
* Percentage of families served
* High priority family count
* Shelter occupancy rate
* Average inventory remaining

## Data Storage

All data is stored in JSON files.

```text
data/
├── families.json
├── inventory.json
├── shelters.json
└── distribution.json
```

The application loads existing data at startup and saves updated information before exiting.

## Data Structures Used

* **List**: store families, shelters, inventory, and distribution records
* **Tuple**: store fixed values such as damage levels and package types
* **Set**: prevent duplicate relief distribution
* **Dictionary**: store record details as key-value pairs

## Object-Oriented Design

### Family

Stores:

* Family ID
* Head name
* Phone
* District
* Village
* Members
* Damage level
* Shelter needed
* Relief status

### InventoryItem

Stores:

* Item name
* Quantity

### Shelter

Stores:

* Shelter ID
* Shelter name
* District
* Capacity
* Occupied seats

### Distribution

Stores:

* Family ID
* Distributed items
* Quantity
* Date

### ReliefManager

Handles:

* All module coordination
* JSON load/save
* Reports
* Statistics
* Overall workflow

## Main Menu

```text
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
```

## Project Structure

```text
ReliefLink/
├── main.py
├── manager.py
├── models.py
├── validation.py
├── file_handler.py
├── statistics.py
├── menu.py
├── utils.py
├── data/
│   ├── families.json
│   ├── inventory.json
│   ├── shelters.json
│   └── distribution.json
└── README.md
```

## Validation and Exception Handling

The system handles:

* Invalid menu choices
* Invalid numeric input
* Duplicate Family IDs
* Missing JSON files
* Empty JSON files
* Corrupted JSON data
* Negative quantities
* Shelter capacity overflow
* Invalid phone numbers

## Team Members and Responsibilities

### Sazid Ahmed Ekram

* Overall project architecture
* Main menu and application flow
* ReliefManager implementation
* Module integration
* Git repository management
* Final testing
* Documentation and presentation

### Easha

* Family class
* Add family
* View family
* Search family
* Update family
* Delete family
* Input validation
* Duplicate ID prevention

### Borshon

* Inventory management
* Shelter management
* Shelter allocation
* Capacity validation
* Inventory CRUD

### Anurag

* JSON file handling
* Exception handling
* Report generation
* Distribution history
* NumPy statistical analysis
* Data persistence

## Future Improvements

* Tkinter GUI version
* QR code family identification
* Role-based login system
* PDF report generation
* SMS notification
* Barcode-based inventory
* Cloud database integration
* Mobile application
* GIS map integration

## Course Learning Outcomes

This project demonstrates:

* Variables and data types
* Operators
* Conditional statements
* Loops
* Functions
* Object-oriented programming
* Lists
* Tuples
* Sets
* Dictionaries
* JSON file handling
* Exception handling
* NumPy
* Modular programming

## License

This project is developed for academic purposes as part of the **Programming in Python** mid-term project.
