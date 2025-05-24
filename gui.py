import tkinter as tk
from tkinter import scrolledtext, ttk
import pandas as pd
import time

class FullScreenApp:
    def __init__(self, root):
        self.root = root
        self.root.attributes('-fullscreen', True)
        self.root.bind('<F11>', self.toggle_fullscreen)
        self.root.bind('<Escape>', self.end_fullscreen)

        # Create PanedWindow with vertical orientation
        self.paned_window = tk.PanedWindow(root, orient=tk.VERTICAL)
        self.paned_window.pack(expand=True, fill='both')

        # Information Label
        self.info_label = tk.Label(root, text="Press F11 to toggle fullscreen. Press Esc to exit fullscreen.", bg="lightgray", font=("Arial", 12))
        self.info_label.pack(side=tk.TOP, fill=tk.X)

        # Text Frame
        self.text_frame = tk.Frame(self.paned_window)
        self.text_widget = scrolledtext.ScrolledText(self.text_frame, wrap=tk.WORD, font=("Courier New", 16))
        self.text_widget.pack(expand=True, fill='both')
        self.text_frame.pack(fill='both')
        
        # Table Frame
        self.table_frame = tk.Frame(self.paned_window)
        self.tree = ttk.Treeview(self.table_frame, columns=(), show='headings')
        self.tree.pack(expand=True, fill='both')
        self.table_frame.pack(fill='both')

        # Add frames to PanedWindow
        self.paned_window.add(self.text_frame, minsize=400)  # Allocate more space initially to the text frame
        self.paned_window.add(self.table_frame, minsize=300)  # Allocate less space initially to the table frame

        # Close Button
        self.close_button = tk.Button(root, text="Close", command=self.end_fullscreen, bg="red", fg="white")
        self.close_button.pack(side=tk.BOTTOM, pady=10)

        # Initialize data update
        self.update_display()
        self.update_data()

    def toggle_fullscreen(self, event=None):
        self.root.attributes('-fullscreen', not self.root.attributes('-fullscreen'))

    def end_fullscreen(self, event=None):
        self.root.attributes('-fullscreen', False)
        self.root.quit()

    def update_display(self):
        self.text_widget.delete(1.0, tk.END)

        infos = self.read_file('infos.txt')
        self.text_widget.insert(tk.END, "Infos.txt Content:\n")
        self.text_widget.insert(tk.END, infos)
        
        # Schedule the next update
        self.root.after(30000, self.update_display)  # Update every 30 seconds
    
    def update_data(self):
        columns = self.get_csv_columns('backup.csv')
        self.tree['columns'] = columns
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor='center')

        self.load_csv_data('backup.csv')
        self.root.after(30000, self.update_data)  # Update every 30 seconds

    def get_csv_columns(self, filename):
        encodings = ['utf-8', 'ISO-8859-1', 'cp1252']
        for enc in encodings:
            try:
                df = pd.read_csv(filename, encoding=enc, nrows=1)
                return list(df.columns)
            except UnicodeDecodeError:
                continue
            except IOError:
                time.sleep(1)
        return []

    def load_csv_data(self, filename):
        self.tree.delete(*self.tree.get_children())
        encodings = ['utf-8', 'ISO-8859-1', 'cp1252']
        for enc in encodings:
            try:
                df = pd.read_csv(filename, encoding=enc)
                for _, row in df.tail(10).iterrows():
                    self.tree.insert("", "end", values=list(row))
                break
            except UnicodeDecodeError:
                continue
            except IOError:
                time.sleep(1)

    def read_file(self, filename):
        while True:
            try:
                with open(filename, 'r', encoding='utf-8') as file:
                    lines = file.readlines()
                return ''.join(lines[:4])  # Return the first 4 lines
            except IOError:
                time.sleep(1)
            except UnicodeDecodeError:
                try:
                    with open(filename, 'r', encoding='ISO-8859-1') as file:
                        lines = file.readlines()
                    return ''.join(lines[:4])
                except Exception as e:
                    return f"Error: Could not read file. {str(e)}"

if __name__ == "__main__":
    root = tk.Tk()
    app = FullScreenApp(root)
    root.mainloop()
