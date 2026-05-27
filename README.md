# PhoneBook

A simple phonebook application built with **Python** and **CustomTkinter (CTK)**, backed by an **SQLite** database.  
This project provides both a **CLI interface** and a **GUI interface** for managing contacts in a lightweight and practical way.

---

## Overview

**PhoneBook** is a contact management application that allows users to store and manage basic contact information such as:

- Name
- Phone number
- Email address
- Physical address

The project is designed as a small but functional desktop/terminal application using:

- Python for core logic
- SQLite for persistent local storage
- Tkinter / CustomTkinter for the graphical interface

---

## Features

- Add new contacts
- Search for a contact by email
- Edit existing contacts
- Delete contacts
- Persistent data storage with SQLite
- Command-line interface support
- Graphical interface support with CustomTkinter

---

## Tech Stack

- **Python 3**
- **SQLite3**
- **Tkinter**
- **CustomTkinter**

---

## Project Structure

```bash
PhoneBook/
├── main.py          # CLI entry point
├── functions.py     # CRUD operations and database logic
├── database.py      # SQLite database wrapper
├── ui.py            # GUI application using CustomTkinter
├── phonebook.db     # SQLite database file
└── __pycache__/     # Python cache files
```

---

## How It Works

### CLI Version
The CLI application is started from `main.py`.

It prints a welcome message and accepts one of the following commands:

- `add`
- `get`
- `edit`
- `remove`

These commands are mapped to the corresponding functions in `functions.py`:

- `add` → `creat_contact()`
- `get` → `get_contact()`
- `edit` → `edit_contact()`
- `remove` → `delete_contact()`

### GUI Version
The GUI is implemented in `ui.py` using `customtkinter`.

It opens a window titled:

- **Phonebook Manager**

Default window settings:

- Size: `700x550`
- Resizable: `False`
- Theme: `light`
- Color theme: `blue`

---

## Database

The application uses an SQLite database named:

```bash
phonebook.db
```

A `contacts` table is created automatically if it does not exist.

### Table Schema

| Column  | Type    | Description |
|--------|---------|-------------|
| id      | INTEGER | Primary key |
| name    | TEXT    | Contact name |
| phone   | TEXT    | Phone number |
| email   | TEXT    | Email address |
| address | TEXT    | Physical address |

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Shayanrsln/PhoneBook.git
cd PhoneBook
```

### 2. Create a virtual environment (optional)

#### Windows
```bash
python -m venv venv
venv\Scriptsctivate
```

#### macOS / Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install customtkinter
```

> Note: `sqlite3` and `tkinter` are usually included with the standard Python installation.

---

## Usage

### Run the CLI version

```bash
python main.py
```

Example prompt:

```bash
welcome to your phonebook
[get | add | edit | remove]
```

### Run the GUI version

```bash
python ui.py
```

---

## Notes

- The project uses some function names with intentional spelling as they appear in the source code, such as:
  - `creat_contact()`
  - `creat_table()`
- The database file is created locally, so no external server is required.
- The repository currently includes a `phonebook.db` file and Python cache directory `__pycache__`.

---

## Acknowledgements

Special thanks to the following projects and communities:

- **Python** — for the programming language used to build this application
- **SQLite** — for the embedded database engine
- **Tkinter** — for the standard GUI foundation
- **CustomTkinter** — for the modern GUI styling
- **Open-source community** — for making learning and development easier

---
## Acknowledgement

Special thank to my colleague **Amirhoosein Ranjbar** for inspiration.