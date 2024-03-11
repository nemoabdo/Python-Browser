import tkinter as tk
from tkinter import ttk
import webbrowser

class SimpleBrowserApp:
    def __init__(self, master):
        self.master = master
        master.title("Simple Browser")

        self.url_label = ttk.Label(master, text="Enter URL:")
        self.url_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.url_entry = ttk.Entry(master, width=40)
        self.url_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.open_button = ttk.Button(master, text="Open Browser", command=self.open_browser)
        self.open_button.grid(row=1, column=0, columnspan=2, pady=10)

    def open_browser(self):
        url = self.url_entry.get()
        try:
            webbrowser.open(url)
        except Exception as e:
            print(f"Error opening the web browser: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleBrowserApp(root)
    root.mainloop()
