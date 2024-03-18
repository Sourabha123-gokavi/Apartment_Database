import random
import sqlite3
conn = sqlite3.connect('DBT24_A1_PES1UG21CS608_Sourabha_Gokavi.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS Tenants
            (tenant_id INTEGER PRIMARY KEY,
            name TEXT,
            apartment_no TEXT,
            contact_number TEXT)''')

c.execute('''CREATE TABLE IF NOT EXISTS Apartments
            (apartment_no TEXT PRIMARY KEY,
            num_bedrooms INTEGER,
            rent_amount REAL)''')

c.execute('''CREATE TABLE IF NOT EXISTS MaintenanceRequests
            (request_id INTEGER PRIMARY KEY,
            apartment_no TEXT,
            issue_description TEXT,
            request_date DATE,
            status TEXT)''')

c.execute('''CREATE TABLE IF NOT EXISTS Payments
            (payment_id INTEGER PRIMARY KEY,
            tenant_id INTEGER,
            amount REAL,
            payment_date DATE)''')

c.execute('''CREATE TABLE IF NOT EXISTS Employees
            (employee_id INTEGER PRIMARY KEY,
            name TEXT,
            position TEXT,
            contact_number TEXT)''')

conn.commit()
conn.close()