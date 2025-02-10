
import tkinter as tk
from tkinter import Toplevel, messagebox
import sqlite3

# Database File
DB_FILE = "sales.db"

# Function to connect to the database
def connect_db():
    return sqlite3.connect(DB_FILE)

# Function to create tables
def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    # Create Sales table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer TEXT NOT NULL,
            product TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL
        )
    """)

    # Create Goods/Stock table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS stock (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product TEXT NOT NULL,
            price REAL NOT NULL
        )
    """)

    conn.commit()
    conn.close()

# Function to add a sale
def add_sale():
    customer = entry_customer.get()
    product = entry_product.get()
    quantity = entry_quantity.get()
    price = entry_price.get()

    if not (customer and product and quantity and price):
        messagebox.showerror("Error", "All fields are required!")
        return

    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO sales (customer, product, quantity, price) VALUES (?, ?, ?, ?)", 
                       (customer, product, int(quantity), float(price)))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Sale added successfully!")
        entry_customer.delete(0, tk.END)
        entry_product.delete(0, tk.END)
        entry_quantity.delete(0, tk.END)
        entry_price.delete(0, tk.END)
        load_sales()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to load sales into the Listbox
def load_sales():
    listbox_sales.delete(0, tk.END)
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, customer, product, quantity, price FROM sales")
    rows = cursor.fetchall()
    conn.close()

    for row in rows:
        listbox_sales.insert(tk.END, f"ID: {row[0]} | {row[1]} - {row[2]} ({row[3]} pcs) - ${row[4]:.2f}")

# Function to add a product to the stock
def add_stock(product, price):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO stock (product, price) VALUES (?, ?)", (product, price))
    conn.commit()
    conn.close()

# Function to open a temporary window showing the Price List
def open_price_list():
    temp_window = Toplevel(root)  # Create a new top-level window
    temp_window.title("Price List")
    temp_window.geometry("300x250")

    tk.Label(temp_window, text="Product Price List", font=("Arial", 12)).pack(pady=10)
    
    listbox_price = tk.Listbox(temp_window, width=40)
    listbox_price.pack(pady=5)

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT product, price FROM stock")
    rows = cursor.fetchall()
    conn.close()

    for row in rows:
        listbox_price.insert(tk.END, f"{row[0]} - ${row[1]:.2f}")

    tk.Button(temp_window, text="Close", command=temp_window.destroy).pack(pady=10)

# Create GUI window
root = tk.Tk()
root.title("Sales Management")
root.geometry("400x400")

# Labels and Entry Fields
tk.Label(root, text="Customer:").grid(row=0, column=0, padx=10, pady=5)
entry_customer = tk.Entry(root)
entry_customer.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Product:").grid(row=1, column=0, padx=10, pady=5)
entry_product = tk.Entry(root)
entry_product.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Quantity:").grid(row=2, column=0, padx=10, pady=5)
entry_quantity = tk.Entry(root)
entry_quantity.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Price:").grid(row=3, column=0, padx=10, pady=5)
entry_price = tk.Entry(root)
entry_price.grid(row=3, column=1, padx=10, pady=5)

# Buttons
tk.Button(root, text="Add Sale", command=add_sale).grid(row=4, column=0, columnspan=2, pady=10)
tk.Button(root, text="View Price List", command=open_price_list).grid(row=5, column=0, columnspan=2, pady=5)

# Sales Listbox
listbox_sales = tk.Listbox(root, width=50)
listbox_sales.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

# Initialize database and load sales
create_tables()
load_sales()

# Sample Stock Data (add only once)
add_stock("Laptop", 1500)
add_stock("Smartphone", 800)
add_stock("Tablet", 1200)
add_stock("Headphones", 200)

# Run the Tkinter event loop
root.mainloop()