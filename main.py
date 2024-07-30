import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from ttkthemes import ThemedTk
import webbrowser
import requests
from datetime import datetime

# Constants
USERNAME = "nayradrian"
TOKEN = "hkKdfhdasiHlg931tyaw412s"
GRAPH_ID = "graph1"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
HEADERS = {"X-USER-TOKEN": TOKEN}
GRAPH_URL = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}.html"


class PixelaApp:
    def __init__(self, root):
        self.root = root
        self.root.title(f"{USERNAME}'s Tracker")

        # Title header
        self.title_label = ttk.Label(self.root, text="Jogging Tracker", font=("Helvetica", 18, "bold"))
        self.title_label.pack(pady=10)

        # Graph link
        self.graph_link = ttk.Label(self.root, text="View Graph", foreground="blue", cursor="hand2",
                                    font=("Helvetica", 14))
        self.graph_link.pack()
        self.graph_link.bind("<Button-1>", self.open_graph_link)

        # Add section
        self.add_frame = ttk.LabelFrame(self.root, text="Add Pixel")
        self.add_frame.pack(pady=10, padx=10, fill="both", expand="yes")

        self.date_label = ttk.Label(self.add_frame, text="Date (YYYYMMDD):")
        self.date_label.grid(row=0, column=0, padx=5, pady=5)
        self.date_entry = ttk.Entry(self.add_frame)
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)

        self.quantity_label = ttk.Label(self.add_frame, text="Distance:")
        self.quantity_label.grid(row=1, column=0, padx=5, pady=5)
        self.quantity_entry = ttk.Entry(self.add_frame)
        self.quantity_entry.grid(row=1, column=1, padx=5, pady=5)

        self.add_button = ttk.Button(self.add_frame, text="Add", command=self.add_pixel)
        self.add_button.grid(row=2, columnspan=2, pady=10)

        # Update section
        self.update_frame = ttk.LabelFrame(self.root, text="Update Pixel")
        self.update_frame.pack(pady=10, padx=10, fill="both", expand="yes")

        self.update_date_label = ttk.Label(self.update_frame, text="Date (YYYYMMDD):")
        self.update_date_label.grid(row=0, column=0, padx=5, pady=5)
        self.update_date_entry = ttk.Entry(self.update_frame)
        self.update_date_entry.grid(row=0, column=1, padx=5, pady=5)

        self.new_quantity_label = ttk.Label(self.update_frame, text="New Distance:")
        self.new_quantity_label.grid(row=1, column=0, padx=5, pady=5)
        self.new_quantity_entry = ttk.Entry(self.update_frame)
        self.new_quantity_entry.grid(row=1, column=1, padx=5, pady=5)

        self.update_button = ttk.Button(self.update_frame, text="Update", command=self.update_pixel)
        self.update_button.grid(row=2, columnspan=2, pady=10)

        # Delete section
        self.delete_frame = ttk.LabelFrame(self.root, text="Delete Pixel")
        self.delete_frame.pack(pady=10, padx=10, fill="both", expand="yes")

        self.delete_date_label = ttk.Label(self.delete_frame, text="Date (YYYYMMDD):")
        self.delete_date_label.grid(row=0, column=0, padx=5, pady=5)
        self.delete_date_entry = ttk.Entry(self.delete_frame)
        self.delete_date_entry.grid(row=0, column=1, padx=5, pady=5)

        self.delete_button = ttk.Button(self.delete_frame, text="Delete", command=self.delete_pixel)
        self.delete_button.grid(row=1, columnspan=2, pady=10)

    def open_graph_link(self, event):
        webbrowser.open(GRAPH_URL)

    def validate_date(self, date_text):
        try:
            datetime.strptime(date_text, '%Y%m%d')
            return True
        except ValueError:
            return False

    def add_pixel(self):
        date = self.date_entry.get()
        if not self.validate_date(date):
            messagebox.showerror("Invalid Date", "Please enter a valid date in YYYYMMDD format.")
            return

        quantity = self.quantity_entry.get()
        pixel_data = {"date": date, "quantity": quantity}
        response = requests.post(url=f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}", json=pixel_data,
                                 headers=HEADERS)
        messagebox.showinfo("Add Pixel", "Pixel Added")

    def update_pixel(self):
        date = self.update_date_entry.get()
        if not self.validate_date(date):
            messagebox.showerror("Invalid Date", "Please enter a valid date in YYYYMMDD format.")
            return

        new_quantity = self.new_quantity_entry.get()
        update_data = {"quantity": new_quantity}
        response = requests.put(url=f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{date}", json=update_data,
                                headers=HEADERS)
        messagebox.showinfo("Update Pixel", "Pixel Updated")

    def delete_pixel(self):
        date = self.delete_date_entry.get()
        if not self.validate_date(date):
            messagebox.showerror("Invalid Date", "Please enter a valid date in YYYYMMDD format.")
            return

        response = requests.delete(url=f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{date}", headers=HEADERS)
        messagebox.showinfo("Delete Pixel", "Pixel Deleted")


# Main
root = ThemedTk(theme="breeze")
app = PixelaApp(root)
root.mainloop()
