
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import requests

# Function to create an event
def create_event():
    title = title_entry.get()
    description = description_entry.get()
    
    date_input = date_entry.get()
    
    # Convert date input to ISO 8601 format
    try:
        date = datetime.strptime(date_input, "%Y-%m-%d %H:%M:%S").isoformat()
    except ValueError:
        messagebox.showerror("Error", "Invalid date format. Please use YYYY-MM-DD HH:MM:SS")
        return
    
    data = {
        "title": title,
        "description": description,
        "date": date
    }
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
            events_text.insert(tk.END, f"ID: {event['id']}, Title: {event['title']}, Description: {event['description']}, Date: {event['date']}, Category: {event['category']}\n")
    else:
        messagebox.showerror("Error", f"Failed to get events: {response.text}")

# Function to update an event
def update_event():
    event_id = event_id_entry.get()
    title = title_entry.get()
    description = description_entry.get()
    date = date_entry.get()
    data = {
        "title": title,
        "description": description,
        "date": date
    }
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

# Create the main window
root = tk.Tk()
root.title("Event Management Service")
root.geometry("600x600") 

# Create input fields and labels
tk.Label(root, text="Event ID").grid(row=0, column=0)
event_id_entry = tk.Entry(root)
event_id_entry.grid(row=0, column=1)

tk.Label(root, text="Title").grid(row=1, column=0)
title_entry = tk.Entry(root)
title_entry.grid(row=1, column=1)

tk.Label(root, text="Description").grid(row=2, column=0)
description_entry = tk.Entry(root)
description_entry.grid(row=2, column=1)

tk.Label(root, text="Date:YYYY-MM-DD HH:MM:SS").grid(row=3, column=0)
date_entry = tk.Entry(root)
date_entry.grid(row=3, column=1)

# Create buttons for each API operation
tk.Button(root, text="Create Event", command=create_event).grid(row=4, column=0)
tk.Button(root, text="Get All Events", command=get_all_events).grid(row=4, column=1)
tk.Button(root, text="Update Event", command=update_event).grid(row=5, column=0)
tk.Button(root, text="Delete Event", command=delete_event).grid(row=5, column=1)

# Create a text widget to display events
events_text = tk.Text(root, height=30, width=60)
events_text.grid(row=6, column=0, columnspan=2)

# Run the main loop
root.mainloop()