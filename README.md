# ReliefLink – Disaster Relief & Shelter Management System

**ReliefLink** is a console-based Python application for managing disaster relief operations, including affected family registration, relief inventory, shelter allocation, and statistical reporting.

## Project Overview

Floods, cyclones, landslides, and other natural calamities impact many households annually in Bangladesh. Relief agencies normally handle beneficiary registration, distribution of relief materials, and accommodation manually, which may cause duplications in beneficiary registration, wrong relief material distribution, insufficient stock of relief items, and poor reporting.

ReliefLink is a solution that addresses all of these issues through a straightforward command-line interface that saves data using JSON files and NumPy for analysis.

## Objectives

* Digitize disaster relief management
* Prevent duplicate family registration and relief distribution
* Maintain relief inventory efficiently
* Allocate shelters based on available capacity
* Generate useful statistical reports using NumPy
* Store all information permanently using JSON files

## Target Users

* Relief organizations such as As Sunnah Foundation
* Volunteers
* Disaster management teams
* Local government authorities

## Technologies Used

* Python 3
* NumPy
* JSON
* Object-Oriented Programming (OOP)
* Console-based interface
* PyCharm

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
* View families in shelters

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
* Children
* Elderly
* Disabled members
* Damage level
* Shelter needed
* Relief status

### InventoryItem

Stores:

* Item id
* Item name
* Quantity
* Unit
* Minimum stock

### Shelter

Stores:

* Shelter ID
* Shelter name
* District
* Capacity
* Occupied seats
* Familes

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
├── family_manager.py
├── inventory_management.py
├── inventory_manager.py
├── models.py
├── modules.py
├── file_handler.py
├── statistics.py
├── relief_distribution.py
├── reports.py
├── shelter_management.py
├── shelter_manager.py
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
* Shelter management implementation


### Easha

* Family management implementation
* Family CRUD

### Borshon

* Inventory management
* Inventory CRUD

### Anurag

* JSON file handling
* Report generation
* Distribution history
* NumPy statistical analysis

## Future Improvements

* Tkinter or PyQt5 GUI version
* Web based version
* Mobile application
* QR code family identification
* Role-based login system
* PDF report generation
* SMS notification
* Barcode-based inventory
* Cloud database integration
* GIS map integration


## License

This project is developed for academic purposes as part of the **Programming in Python** mid-term project.
