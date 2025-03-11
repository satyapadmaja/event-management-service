import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import requests
import ttkbootstrap as tb

# Function to create an event
def create_event():
    title = title_entry.get()
    description = description_entry.get()
    date_input = date_entry.get()
    
    try:
        date = datetime.strptime(date_input, "%Y-%m-%d %H:%M:%S").isoformat()
    except ValueError:
        messagebox.showerror("Error", "Invalid date format. Please use YYYY-MM-DD HH:MM:SS")
        return
    
    data = {"title": title, "description": description, "date": date}
    response = requests.post("http://127.0.0.1:5000/events", json=data)
    if response.status_code == 201:
        messagebox.showinfo("Success", "Event created successfully!")
    else:
        messagebox.showerror("Error", f"Failed to create event: {response.text}")

# Function to get all events
def get_all_events():
    response = requests.get("http://127.0.0.1:5000/events")
    if response.status_code == 200:
        events = response.json()
        events_text.delete(1.0, tk.END)
        for event in events:
            events_text.insert(tk.END, f"ID: {event['id']}, Title: {event['title']}, Description: {event['description']}, Date: {event['date']}, Category: {event.get('category', 'N/A')}\n")
    else:
        messagebox.showerror("Error", f"Failed to get events: {response.text}")

# Function to get an event by ID
def get_event_by_id():
    event_id = event_id_entry.get()
    response = requests.get(f"http://127.0.0.1:5000/events/{event_id}")
    if response.status_code == 200:
        event = response.json()
        events_text.delete(1.0, tk.END)
        events_text.insert(tk.END, f"ID: {event['id']}, Title: {event['title']}, Description: {event['description']}, Date: {event['date']}, Category: {event.get('category', 'N/A')}\n")
    else:
        messagebox.showerror("Error", f"Failed to get event: {response.text}")

# Function to update an event
def update_event():
    event_id = event_id_entry.get()
    title = title_entry.get()
    description = description_entry.get()
    date = date_entry.get()
    data = {"title": title, "description": description, "date": date}
    response = requests.put(f"http://127.0.0.1:5000/events/{event_id}", json=data)
    if response.status_code == 200:
        messagebox.showinfo("Success", "Event updated successfully!")
    else:
        messagebox.showerror("Error", f"Failed to update event: {response.text}")

# Function to delete an event
def delete_event():
    event_id = event_id_entry.get()
    response = requests.delete(f"http://127.0.0.1:5000/events/{event_id}")
    if response.status_code == 200:
        messagebox.showinfo("Success", "Event deleted successfully!")
    else:
        messagebox.showerror("Error", f"Failed to delete event: {response.text}")

# Create main window
root = tb.Window(themename="superhero")
root.title("Event Management Service")
root.geometry("700x700")
root.eval('tk::PlaceWindow . center')  # Center the window on the screen

# Create input fields with modern styling
tb.Label(root, text="Event ID", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5)
event_id_entry = tb.Entry(root, width=40)
event_id_entry.grid(row=0, column=1, padx=10, pady=5)

tb.Label(root, text="Title", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5)
title_entry = tb.Entry(root, width=40)
title_entry.grid(row=1, column=1, padx=10, pady=5)

tb.Label(root, text="Description", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=5)
description_entry = tb.Entry(root, width=40)
description_entry.grid(row=2, column=1, padx=10, pady=5)

tb.Label(root, text="Date (YYYY-MM-DD HH:MM:SS)", font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=5)
date_entry = tb.Entry(root, width=40)
date_entry.grid(row=3, column=1, padx=10, pady=5)

# Create stylish buttons
tb.Button(root, text="Create Event", bootstyle="success", command=create_event).grid(row=4, column=0, padx=10, pady=10)
tb.Button(root, text="Get All Events", bootstyle="info", command=get_all_events).grid(row=4, column=1, padx=10, pady=10)
tb.Button(root, text="Get Event by ID", bootstyle="primary", command=get_event_by_id).grid(row=5, column=0, padx=10, pady=10)
tb.Button(root, text="Update Event", bootstyle="warning", command=update_event).grid(row=5, column=1, padx=10, pady=10)
tb.Button(root, text="Delete Event", bootstyle="danger", command=delete_event).grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Create modern text area to display events
events_text = tk.Text(root, height=25, width=80, font=("Arial", 10))
events_text.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

# Run the main loop
root.mainloop()