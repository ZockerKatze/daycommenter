## ik, the programm stores json data kinda unreadable and is kinda inefficient but i threw this together at fucking 3am or somehtin

import tkinter as tk
from tkinter import simpledialog
from calendar import monthcalendar, month_name
import os
import json
from datetime import datetime

## check if the directory is there if not make it

BASE_DIR = "calendar_data"
if not os.path.exists(BASE_DIR):
    os.makedirs(BASE_DIR)

## load data from the json file


def load_data(year, month):
    global folder ## make the variable for folder global to be used in other functions
    folder = os.path.join(BASE_DIR, f"{month_name[month].lower()}_{year}")
    file_path = os.path.join(folder, "data.json") ## define a variable to house the JSON file
    if os.path.exists(file_path): ## if the folder with the JSON file exists
        with open(file_path, "r") as file: ## read the jsonfile
            return json.load(file)
    return {}


## make a function to save data to the JSON file

def save_data(data, year, month): ## parse 3 vars to save_data to be used!
    if not os.path.exists(folder):  # if the folder does not exist then make it
        os.makedirs(folder)
    file_path = os.path.join(folder, "data.json")
    with open(file_path, "w") as file: ## write the data to the file
        json.dump(data, file)


## make the day click function thing


def on_day_click(day_label, day, data, year, month):
    if day == 0:  # Ignore empty cells
        return

    ## in ODC func define savecomment

    def save_comment():
        comment = comment_text.get("1.0", tk.END).strip()
        selected_color = color_var.get()
        if comment:
            data[str(day)] = {"comment": comment, "color": selected_color}
            day_label.config(bg=selected_color)
        else:
            data[str(day)] = {"comment": "", "color": "#FF9999"}  # Light red color in hex
            day_label.config(bg="#FF9999")
        save_data(data, year, month)
        comment_window.destroy()

    ## define a exitcomment function to exit the comment box

    def exit_comment():
        comment_window.destroy()

    # Create a new window for the comment

    comment_window = tk.Toplevel()
    comment_window.title(f"Comment for {month_name[month]} {day}, {year}")
    comment_window.geometry("300x300")

    # Text widget for comment input

    comment_text = tk.Text(comment_window, wrap=tk.WORD, height=10, width=30)
    existing_comment = data.get(str(day), {}).get("comment", "")
    comment_text.insert("1.0", existing_comment)
    comment_text.pack(pady=10)

    # Dropdown for selecting color

    color_frame = tk.Frame(comment_window)
    color_frame.pack(pady=5)

    tk.Label(color_frame, text="Select Color:").pack(side=tk.LEFT, padx=5)

    color_var = tk.StringVar(value=data.get(str(day), {}).get("color", "#FF9999"))
    color_options = ["lightgreen", "#FF9999", "lightblue", "yellow"]
    color_dropdown = tk.OptionMenu(color_frame, color_var, *color_options)
    color_dropdown.pack(side=tk.LEFT)

    # Buttons to save or exit
    button_frame = tk.Frame(comment_window)
    button_frame.pack()

    save_button = tk.Button(button_frame, text="Save", command=save_comment)
    save_button.pack(side=tk.LEFT, padx=5)

    exit_button = tk.Button(button_frame, text="Exit", command=exit_comment)
    exit_button.pack(side=tk.LEFT, padx=5)

# Create calendar for a specific month and year
def create_calendar(root, year, month):
    for widget in root.winfo_children():
        widget.destroy()

    ## make a list for the corresponding week days to be used

    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # Load existing data
    data = load_data(year, month)

    # Generate calendar
    calendar_data = monthcalendar(year, month)

    # Navigation buttons
    def prev_month():
        new_month = month - 1 if month > 1 else 12
        new_year = year - 1 if month == 1 else year
        create_calendar(root, new_year, new_month)

    def next_month():
        new_month = month + 1 if month < 12 else 1
        new_year = year + 1 if month == 12 else year
        create_calendar(root, new_year, new_month)

    def go_to_today():
        today = datetime.today()
        create_calendar(root, today.year, today.month)

    nav_frame = tk.Frame(root)
    nav_frame.grid(row=0, column=0, columnspan=7)

    prev_button = tk.Button(nav_frame, text="<<", command=prev_month)
    prev_button.pack(side=tk.LEFT, padx=5)

    title_label = tk.Label(nav_frame, text=f"{month_name[month]} {year}", font=('Arial', 16, 'bold'))
    title_label.pack(side=tk.LEFT, padx=5)

    next_button = tk.Button(nav_frame, text=">>", command=next_month)
    next_button.pack(side=tk.LEFT, padx=5)

    today_button = tk.Button(nav_frame, text="Today", command=go_to_today)
    today_button.pack(side=tk.LEFT, padx=5)

    # Header row for weekdays
    for col, day in enumerate(days_of_week):
        header = tk.Label(root, text=day, font=('Arial', 12, 'bold'), bg='lightblue', relief='ridge', width=12, height=2)
        header.grid(row=1, column=col)

    # Fill in the calendar
    for row, week in enumerate(calendar_data, start=2):
        for col, day in enumerate(week):
            if day == 0:  # Empty cell for days outside the month
                day_label = tk.Label(root, text="", bg='white', relief='ridge', width=12, height=2)
            else:
                color = data.get(str(day), {}).get("color", "#FF9999")  # Default to light red in hex
                day_label = tk.Label(root, text=str(day), bg=color, relief='ridge', width=12, height=2)
                day_label.bind("<Button-1>", lambda event, label=day_label, d=day: on_day_click(label, d, data, year, month))

            day_label.grid(row=row, column=col)

# Main function
def main():
    year, month = 2025, 1

    # Create root window
    root = tk.Tk()
    root.title("Calendar")

    # Initial calendar setup
    create_calendar(root, year, month)

    # Run the main loop
    root.mainloop()

if __name__ == "__main__":
    main()
