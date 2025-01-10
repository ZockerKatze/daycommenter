# Calendar with Comments and Color-Coding

A Python-based calendar application that allows users to:
- View a calendar for any month and year.
- Add, edit, and save comments for specific days.
- Assign colors to days for easy visual categorization.
- Navigate through months and go directly to the current month.

The application uses **Tkinter** for its graphical user interface and stores calendar data in JSON files.

---

## Features

1. **Interactive Calendar**:
   - Click on any day to add or edit a comment.
   - Assign a custom color to each day.
2. **Data Persistence**:
   - Comments and colors are saved locally in JSON files organized by year and month.
   - Automatically creates directories and files if they don’t exist.
3. **Navigation**:
   - Move between months using navigation buttons.
   - Jump directly to the current month.

---

## Requirements

- Python 3.x
- Required modules:
  - `tkinter` (usually bundled with Python)
  - `json`
  - `os`
  - `calendar`
  - `datetime`

---

## How to Run

1. Clone this repository or copy the program code.
2. Run the Python script:
   ```bash
   python calendar_app.py
